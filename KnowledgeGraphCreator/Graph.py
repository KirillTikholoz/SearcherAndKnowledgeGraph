import time
import json
from langchain.chat_models import ChatOpenAI
from langchain.graphs import Neo4jGraph
from langchain_core.prompts import ChatPromptTemplate
import openai

url = "neo4j+s://4eab2c29.databases.neo4j.io"
username ="neo4j"
password = "PZK_ZC9gVpeKe11nHItgyL4tFTlaoFD0u39nQeu8QcQ"
graph = Neo4jGraph(
 url=url,
 username=username,
 password=password
)


from langchain.graphs.graph_document import (
 Node as BaseNode,
 Relationship as BaseRelationship,
 GraphDocument,
)

from langchain.schema import Document
from typing import List, Dict, Any, Optional
from langchain.pydantic_v1 import Field, BaseModel


class Property(BaseModel):
  """Единое свойство, состоящее из ключа и значения"""
  key: str = Field(..., description="key")
  value: str = Field(..., description="value")

class Node(BaseNode):
 properties: Optional[List[Property]] = Field(
        None, description="Список свойств узла")

class Relationship(BaseRelationship):
 properties: Optional[List[Property]] = Field(
        None, description="Список свойств взаимосвязи"
    )

class KnowledgeGraph(BaseModel):
    """Generate a knowledge graph with entities and relationships."""
    nodes: List[Node] = Field(
        ..., description="List of nodes in the knowledge graph")
    rels: List[Relationship] = Field(
        ..., description="List of relationships in the knowledge graph")

#-----------------------------------------------------------

def format_property_key(s: str) -> str:
    words = s.split()
    if not words:
        return s
    first_word = words[0].lower()
    capitalized_words = [word.capitalize() for word in words[1:]]
    return "".join([first_word] + capitalized_words)

def props_to_dict(props) -> dict:
    """Convert properties to a dictionary."""
    properties = {}
    if not props:
      return properties
    for p in props:
        properties[format_property_key(p.key)] = p.value
    return properties

def map_to_base_node(node: Node) -> BaseNode:
    """Map the KnowledgeGraph Node to the base Node."""
    properties = props_to_dict(node.properties) if node.properties else {}
    # Add name property for better Cypher statement generation
    properties["name"] = node.id.title()
    return BaseNode(
        id=node.id.title(), type=node.type.capitalize(), properties=properties
    )

def map_to_base_relationship(rel: Relationship) -> BaseRelationship:
    """Map the KnowledgeGraph Relationship to the base Relationship."""
    source = map_to_base_node(rel.source)
    target = map_to_base_node(rel.target)
    properties = props_to_dict(rel.properties) if rel.properties else {}
    return BaseRelationship(
        source=source, target=target, type=rel.type, properties=properties
    )

#-----------------------------------------------------------

import os
from langchain.chains.openai_functions import (
    create_openai_fn_chain,
    create_structured_output_chain,
)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

os.environ["OPENAI_API_KEY"] = "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"
llm = ChatOpenAI(model="gpt-3.5-turbo-16k", temperature=0)

def get_extraction_chain(
    allowed_nodes: Optional[List[str]] = None,
    allowed_rels: Optional[List[str]] = None
    ):
        prompt = ChatPromptTemplate.from_messages(
        [(
            "system",
            f"""# Knowledge Graph Instructions for GPT-4
            По возможности узлы и отношения в графе должны быть предоставлены на русском языке
        ## 1. Overview
        You are a top-tier algorithm designed for extracting information in structured formats to build a knowledge graph.
        - **Nodes** represent entities and concepts. They're akin to Wikipedia nodes.
        - The aim is to achieve simplicity and clarity in the knowledge graph, making it accessible for a vast audience.
        ## 2. Labeling Nodes
        - **Consistency**: Ensure you use basic or elementary types for node labels.
         - For example, when you identify an entity representing a person, always label it as **"person"**. Avoid using more specific terms like "mathematician" or "scientist".
        - **Node IDs**: Never utilize integers as node IDs. Node IDs should be names or human-readable identifiers found in the text.
        {'- **Allowed Node Labels:**' + ", ".join(allowed_nodes) if allowed_nodes else ""}
        {'- **Allowed Relationship Types**:' + ", ".join(allowed_rels) if allowed_rels else ""}
        ## 3. Handling Numerical Data and Dates
        - Numerical data, like age or other related information, should be incorporated as attributes or properties of the respective nodes.
        - **No Separate Nodes for Dates/Numbers**: Do not create separate nodes for dates or numerical values. Always attach them as attributes or properties of nodes.
        - **Property Format**: Properties must be in a key-value format.
        - **Quotation Marks**: Never use escaped single or double quotes within property values.
        - **Naming Convention**: Use camelCase for property keys, e.g., `birthDate`.
        ## 4. Coreference Resolution
        - **Maintain Entity Consistency**: When extracting entities, it's vital to ensure consistency.
        If an entity, such as "John Doe", is mentioned multiple times in the text but is referred to by different names or pronouns (e.g., "Joe", "he"), 
        always use the most complete identifier for that entity throughout the knowledge graph. In this example, use "John Doe" as the entity ID. 
        Remember, the knowledge graph should be coherent and easily understandable, so maintaining consistency in entity references is crucial. 
        ## 5. Strict Compliance
        Adhere to the rules strictly. Non-compliance will result in termination."""),
        ("human", "Use the given format to extract information from the following input: {input}"),
        ("human", "Tip: Make sure to answer in the correct format"),
        ])
        return create_structured_output_chain(KnowledgeGraph, llm, prompt, verbose=False)

#-----------------------------------------------------------

def extract_and_store_graph(
    document: Document,
    nodes:Optional[List[str]] = None,
    rels:Optional[List[str]]=None) -> None:

    try:
        # Extract graph data using OpenAI functions
        extract_chain = get_extraction_chain(nodes, rels)
        data = extract_chain.run(input=document.page_content, timeout=10)
        # Construct a graph document
        graph_document = GraphDocument(
            nodes = [map_to_base_node(node) for node in data.nodes],
            relationships = [map_to_base_relationship(rel) for rel in data.rels],
            source = document
        )

        # Store information into a graph
        graph.add_graph_documents([graph_document])

    except openai.RateLimitError as e:
        time.sleep(21)
        print(e)


#-----------------------------------------------------------

from langchain.text_splitter import TokenTextSplitter

file_path = 'C:\Programm2023\WebProg\Scraper\Trevor.json'
with open(file_path, 'r', encoding='utf-8') as file:
    persons = json.load(file)

try:
    for item in persons:
        test_raw_arr = item["Description"]
        document_array = [Document(page_content=text, metadata={"source": "local"}) for text in test_raw_arr]
        raw_documents = document_array

        # Define chunking strategy
        text_splitter = TokenTextSplitter(chunk_size=2048, chunk_overlap=24)

        # Only take the first the raw_documents
        documents = text_splitter.split_documents(raw_documents[1:10])

        from tqdm import tqdm

        for i, d in tqdm(enumerate(documents), total=len(documents)):
            time.sleep(21)
            extract_and_store_graph(d)

except Exception as e:
    print(e)
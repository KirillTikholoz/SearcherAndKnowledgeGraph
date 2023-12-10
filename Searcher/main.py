import Searcher


def main():
    while True:
        fields = []
        print("1. Create Index\n2. Delete Index\n3. Search Articles\n0. Exit")
        choice = input("\nChoose Action\n")
        if choice == "1":
            Searcher.createIndex()
        elif choice == "2":
            Searcher.deleteIndex()
        elif choice == "3":
            flag = True
            while flag == True:
                mode = input("6. Поиск по всем полям\n0. Ввести запрос\n")
                if mode == "6":
                    flag = False
                elif mode == "0":
                    flag = False
                    print("Поиск по полям:")
                    for item in fields:
                        print(item)

            query = input("Введите запрос\n")
            Searcher.searchArticles(fields, query)
        elif choice == "0":
            print("Выход из программы.")
            break

if __name__ == '__main__':
    main()


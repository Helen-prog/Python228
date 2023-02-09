# def add_title():
#     ...


class UserInterface:
    # @add_title('Ввод пользовательских данных')
    def wait_user_answer(self):
        # print(" Ввод пользовательских данных ".center(50, "="))
        print("Действия со статьями:")
        print("1 - создание статьи"
              "\n2 - просмотр статей"
              "\n3 - просмотр определенной статьи"
              "\n4 - удаление статьи"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        # print("=" * 50)
        return user_answer

    # @add_title('Создание статьи:')
    def add_user_article(self):
        dict_article = {
            "название": None,
            "автор": None,
            "количество страниц": None,
            "описание": None
        }
        print(" Создание статьи ".center(50, "="))
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи: ")
        print("=" * 50)
        return dict_article

    # @add_title('Список статей:')
    def show_all_articles(self, articles):
        print(" Список статей: ".center(50, "="))
        for ind, article in enumerate(articles, start=1):
            print(f"{ind}. {article}")
        print("=" * 50)

# Создать приложение телефонная книга. класс Contact имеет следующие поля:
# Имя, фамилия, телефонный номер - обязательные поля;
# избранный контакт - необязательное поле. По умолчанию False;
# Дополнительная информация(email, список дополнительных номеров, ссылки на соцсети) - необходимо использовать *args, **kwargs.
# Переопределить "магический" метод str для красивого вывода контакта. Вывод контакта должен быть следующим
#
# jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
# print(jhon)

# Вывод:
# Имя: Jhon
# Фамилия: Smith
# Телефон: +71234567809
# В избранных: нет
# Дополнительная информация:
# 	 telegram : @jhony
# 	 email : jhony@smith.com

# класс PhoneBook:
# Название телефонной книги - обязательное поле;
# Телефонная книга должна работать с классами Contact.
# Методы:
#
# Вывод контактов из телефонной книги;
# Добавление нового контакта;
# Удаление контакта по номеру телефона;
# Поиск всех избранных номеров
# Поиск контакта по имени и фамилии

# *3. Продвинутый print (необязательное задание) Разработать свою реализацию функции print - adv_print. Она ничем не должна отличаться от классической функции кроме трех новых необязательных аргументов:
#
# start - с чего начинается вывод. По умолчанию пустая строка;
# max_line - максимальная длин строки при выводе. Если строка превыщает max_line, то вывод автоматически переносится на новую строку;
# in_file - аргумент, определяющий будет ли записан вывод ещё и в файл. Сигнатура функции должна быть такой
# def adv_print(*args, **kwargs)

class Contact:
    def __init__(self, name, surname, phone_number, favorite=False, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.favorite = favorite
        self.kwargs = kwargs

    def __str__(self):
        return f'Имя: {self.name}\n' \
            f'Фамилия: {self.surname}\n' \
            f'Номер телефона: {self.phone_number}\n' \
            f'Избранный: {self.favorite}, необходимо отредактировать вывод\n' \
            f'Дополнительная информация: {self.kwargs}, необходимо отредактировать вывод\n' \

class PhoneBook(Contact):
    contact_list = []

    def get_contact(self):
        pass

    def add_contact(self):
        pass

    def del_contact_for_number(self):
        pass

    def search_favorite(self):
        pass

    def search_for_name_and_surname(self):
        pass


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    paul = PhoneBook('Paul', 'Xxx', '+7**********', True, telegram='@paul', email='xxx@mail.com', vk='vk.com',
                   facebook='facebook.com')
    print(jhon)
    print(paul)

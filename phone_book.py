class Contact:
    def __init__(self, name, surname, phone_number, favorite=False, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.favorite = favorite
        self.kwargs = kwargs

    def __str__(self):
        print(f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}\n'
              f'Номер телефона: {self.phone_number}')
        if self.favorite is False:
            print('Избранный: нет')
        else:
            print('Избранный: да')
        print('Дополнительная информация:')
        for elem, value in self.kwargs.items():
            print('\t', elem, ':', value)
        return ''

class PhoneBook:
    contact_list = []

    def __init__(self, name_book):
        self.name_book = name_book

    def get_contact(self):
        if len(self.contact_list) == 0:
            print('Книга пуста')
            self.contact_list.append(get_new_contact())
        else:
            for contact in self.contact_list:
                print('\n', contact)
        return

    def add_contact(self, who_add):
        self.contact_list.append(who_add)
        print('Контакт добавлен\n')
        return

    def del_contact_for_number(self, phone_number):
        for contact in self.contact_list:
            if phone_number == contact.phone_number:
                self.contact_list.remove(contact)
        print('Контакт удален\n')
        return

    def get_favorite(self):
        for contact in self.contact_list:
            if contact.favorite is True:
                print(contact.name, contact.surname, contact.phone_number)
        return

    def search_for_name_and_surname(self, name, surname):
        for contact in self.contact_list:
            if name == contact.name and surname == contact.surname:
                print(contact)
        return

def get_favorite():
    favorite = input('Добавить в избранные? +/- ')
    if favorite is '+':
        favorite = True
    elif favorite is '-':
        favorite = False
    else:
        print('Некорректные данные!!!')
        favorite = get_favorite()
    return favorite

def get_new_contact():
    print('Введите данные нового контакта:')
    name = input('Имя:')
    surname = input('Фамилия:')
    phone_number = input('Номер телефона:')
    favorite = get_favorite()
    email = input('email')
    telegram = input('telegram')
    facebooke = input('facebook')
    vkontakte = input('vkontakte')
    add_phone1 = input('add_phone1')
    add_phone2 = input('add_phone2')
    new_contact = Contact(name, surname, phone_number, favorite, email=email, telegram=telegram, facebooke=facebooke,
                          vkontakte=vkontakte, add_phone1=add_phone1, add_phone2=add_phone2)
    return new_contact

def main():
    tel_book = PhoneBook(input('Введите название телефонной книги: '))
    print(f'Книга {tel_book.name_book} создана')
    print('Доступные команды:\n'
          '"a" - вывести список всех контактов\n'
          '"b" - добавить контакт\n'
          '"c" - удалить по номеру телефона\n'
          '"d" - избранные\n'
          '"e" - найти по имени и фамилии\n'
          '"q" - выход\n')
    while True:
        input_command = input('Введите команду:')
        if input_command == "a":
            tel_book.get_contact()
        if input_command == "b":
            tel_book.add_contact(get_new_contact())
        if input_command == "c":
            input_phone = input('Введите номер телефона: ')
            tel_book.del_contact_for_number(input_phone)
        if input_command == "d":
            tel_book.get_favorite()
        if input_command == "e":
            input_name = input('Введите имя: ')
            input_surname = input('Введите фамилию: ')
            tel_book.search_for_name_and_surname(input_name, input_surname)
        if input_command == "q":
            break


if __name__ == '__main__':
    main()

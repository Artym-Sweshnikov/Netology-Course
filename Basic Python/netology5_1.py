documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def main_func():
    if command == 'p':
        personal_documents()
    elif command == 's':
        document_location()
    elif command == 'l':
        personal_list_of_worker()
    elif command == 'a':
        add_new_data()
    else:
        print('Вы ввели неверную команду!')


def personal_documents():
    document_number = input("Введите полный номер документа: ")
    document_found = False
    for document in documents:
        if document_number == document['number']:
            document_found = True
            print(document['name'])
    if document_found is False:
        print('Документ не найден')


def document_location(): # Здесь появляется понятие Флаговая переменная
    document_number = input("Введите номер документа: ")
    document_found = False
    for key in directories:
        if document_number in directories[key]:
            document_found = True
            print(key)
    if document_found is False:
        print('Документ не найден')


def personal_list_of_worker():
    for data in documents:
        print(data['type'], end=' ')
        num = data['number']
        person = data['name']
        print(f'"{num}" "{person}"')


def add_new_data():
    type_of_document = input('Введите тип документа: ')
    number_of_document = input('Введите номер документа: ')
    name_of_owner = input('Введите имя владельца: ')
    number_of_shelf = input('Введите номер полки: ')
    if int(number_of_shelf) > 3:
        print('Такой полки нет, введите существующую!')
        add_new_data()
    else:
        documents.append({'type': type_of_document, "number": number_of_document, "name": name_of_owner})
        directories[number_of_shelf].append(number_of_document)
        print('Новые данные успешно добавлены!')


print('ВНИМАНИЕ!!!\nПри вводе данных будьте бдительны!')
command = input('Введите команду: ')
main_func()

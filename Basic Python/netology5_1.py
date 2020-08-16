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


def personal_documents():
    document_number = input("Введите номер документа: ")
    for document in documents:
        # print(document)
        if document_number in document['number']:
            print(document['name'])


def document_location():
    document_number = input("Введите номер документа: ")
    for key in directories:
        if document_number in directories[key]:
            print(key)


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
    documents.append({'type': type_of_document, "number": number_of_document, "name": name_of_owner})
    print(documents)
    directories[number_of_shelf].append(number_of_document)
    print(directories)


command = input('Введите команду: ')
if command == 'p':
    personal_documents()
elif command == 's':
    document_location()
elif command == 'l':
    personal_list_of_worker()
elif command == 'a':
    add_new_data()
else:
    print('ВНИМАНИЕ!!!\nВы ввели неверную команду')

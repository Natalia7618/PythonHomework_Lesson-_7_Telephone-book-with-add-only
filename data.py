import csv

name = ''
surname = ''
phone_number = ''
description = ''

def init (name, surname, phone_number, description):
    name = name
    surname = surname
    phone_number = phone_number
    description = description


def add_member_txt(name, surname, phone_number, description):
    f = open('Phone_book.txt', 'a', encoding ='utf-8')
    f.write(f'Контакт: {name} {surname} {phone_number} - {description}')
    f.write("\n")
    print(f'\nКонтакт {name} {surname} успешно добавлен\n')
    f.close()   
        
def add_member_csv(name, surname, phone_number, description):

    with open("Phone_book.csv", "a", encoding ='utf-8') as fp:
        writer = csv.writer(fp, delimiter='|')

        data = [
            (name, surname, phone_number, description)
        ]

        writer.writerows(data)


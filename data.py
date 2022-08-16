import csv

def add_member_txt(name, surname, phone_number, description):
    f = open('Phone_book.txt', 'a', encoding ='utf-8')
    f.write(f'Контакт: {name} {surname} {phone_number} - {description}')
    f.write("\n")
    f.close()   
        
def add_member_csv(name, surname, phone_number, description):
    data = [(name, surname, phone_number, description)]
    with open("Phone_book.csv", "a", encoding ='utf-8') as fp:
        writer = csv.writer(fp, delimiter='|')
        writer.writerows(data)
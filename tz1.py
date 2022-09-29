class Contact:

    name = ""
    number = ""
    mail = ""

    def __init__(self, name, number, mail):         
        self.name = name
        self.number = number
        self.mail = mail


print('Введите имя файла с базой данных: ')
file_name = str(input())
try:
    file = open(file_name)
    file_lines = file.readlines()
except IOError:
    print("Ошибка чтения файла!")

contact_book = []

for s in file_lines:

    cont = s.split(',')
    print(cont)


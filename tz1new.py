class Contact():
    def __init__(self, fio, tel, pochta):
        self.fio = fio
        self.tel = tel
        self.pochta = pochta


def readbase(nazv, book):
    spisok = open(nazv, 'r').readlines()
    for st in spisok:
        mas = st.split(',')
        x = Contact(mas[0], mas[1], mas[2])
        book.append(x)


def poisktel(tel, book):
    print('Найдено:')
    for chel in book:
        if chel.tel.__contains__(tel):
            print(chel.fio, chel.tel, chel.pochta)
    print()


def poiskpochta(pochta, book):
    print('Найдено:')
    for chel in book:
        if chel.pochta.__contains__(pochta):
            print(chel.fio, chel.tel, chel.pochta)
    print()


def poiskfio(fio, book):
    print('Найдено:')
    chastifio1 = fio.split()
    for chel in book:
        chastifio2 = chel.fio.split()
        fl = False
        for a in chastifio1:
            if fl:
                break
            for b in chastifio2:
                if fl:
                    break
                if a == b:
                    print(chel.fio, chel.tel, chel.pochta)
                    fl = True
    print()

def poiskpustyh(book):
    print('Найдено:')
    for chel in book:
        if chel.tel.strip() == '' or chel.pochta.strip() == '':
            print(chel.fio, chel.tel, chel.pochta)


nazv = input('Напишите название файла:')
spisokkontaktov = []
readbase(nazv, spisokkontaktov)
ans = 'yes'
while ans == 'yes':
    print('Выберите действие:', '1 - Найти телефон', '2 - Найти почту', '3 - Найти имя', '4 - Найти без телефона или почты', sep = '\n')
    num = int(input('Введите номер действия которое выбрали:'))
    if num == 1:
        tel = input('Введите телефон:')
        poisktel(tel, spisokkontaktov)
    elif num == 2:
        pochta = input('Введите почту:')
        poiskpochta(pochta, spisokkontaktov)
    elif num == 3:
        fio = input('Введите имя:')
        poiskfio(fio, spisokkontaktov)
    elif num == 4:
        poiskpustyh(spisokkontaktov)
    else:
        continue

    ans = input('Продолжим? Введите yes для продолжения:')
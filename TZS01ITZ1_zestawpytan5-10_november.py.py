print("Ćw-1")


def register():

    uzytkownicy = {}
    login = input("Utwórz login: ")
    password1 = input("Utwórz hasło: ")
    password2 = input("Powtórz hasło: ")

    # try:
    if not len(login) > 5:
        raise ValueError("Login musi mieć więcej niż 5 znaków")
    if not len(password1) > 6:
        raise ValueError("Hasło musi mieć więcej niż 6 znaków")
    if not password1 == password2:
        raise ValueError("Hasła muszą być takie same")

    print("Zaakceptowano dane logowania")
    uzytkownicy[login] = password1
    print(uzytkownicy)


register()

print("Ćw-2")


def validatelist():
    lista1 = [1, 2, 3, 4, 5]  # funkcja powinna zwrócić (15, 5, 1)
    lista2 = [1]  # funckja powinna zwrócić (1, 1, 1)
    lista3 = []  # funkcja powinna podnieść ValueError
    lista4 = [1, 2, 3, 4, 'a']  # funkcja powinna podnieść ValueError
    #list = [1,"a",3,4,5]

    # print(min(list))

    if len(lista1) == 0:
        raise ValueError("Na liście powinny znajdować się elementy")
    try:

        for i in lista1:
            assert isinstance(i, (int, float))
    except:
        print("Elementy listy powinny być typu int lub float")

    else:
        x = min(lista1)

        y = max(lista1)

        z = sum(lista1)

        mms = [x, y, z]
        print(mms)


validatelist()

print("Ćw-3")


def options():
    uzytkownicy = {}
    print("1.Dodaj użytkownika")
    print("2.Wyświetl uzytkownikow")
    print("3.Zmień hasło użytkownia")
    print("4.Usuń użytkownika")
    print("5.Wyjdź z programu")


while True:

    options()
    option = input("Podaj wybraną opcję: ")

    if option == "1":

        login = input("Podaj nazwę użytkownika: ")
        password1 = input("Podaj hasło: ")
        password2 = input("Powtórz hasło: ")
        users = {}
        users[login] = password1

        if not len(login) > 5:
            raise ValueError("Login musi mieć więcej niż 5 znaków")
        if not len(password1) > 6:
            raise ValueError("Hasło musi mieć więcej niż 6 znaków")
        if not password1 == password2:
            raise ValueError("Hasła muszą być takie same")
    elif option == '2':
        users[login] = password1
        for i in users:
            print("Użytkownicy w bazie: ", (i))
    elif option == '3':
        if input("Podaj swój login: ") in users:
            print("Jesteś zarejestrowany w bazie")
            del users[input("Podaj jeszcze raz login, aby zmienić hasło: ")]
            login1 = input("Podaj login ponownie: ")
            new_password = input("Podaj nowe hasło: ")
            users[login1] = new_password
            print(users)
        else:
            print("Nie zostałeś zarejestrowany w bazie")

    elif option == '4':
        if input("Podaj swój login: ") in users:
            print("Jesteś zarejestrowany w bazie")
            del uzytkownicy[input(
                "Podaj jeszcze raz login, aby usunąć swoje konto: ")]
        else:
            print("Nie zostałeś zarejestrowany w bazie")
    elif option == '5':
        break

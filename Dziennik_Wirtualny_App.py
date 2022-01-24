# Panel wejściowy (logowanie, rejestracja)

users_teachers = {}
users_students = {}
users_parents = {}
baza_ocen = {}
lista_ocen = []
tablica_komunikatów = {}

# _____________________________________________________________________________________________________________________
# Definicje logowania nauczyciela, ucznia, rodzica


def logowanie_nauczyciela():
    ("______________________________________________________________")
    login_t = input("Podaj swój login: ")
    password_t = input("Podj swoje hasło: ")
    if login_t in users_teachers.keys() and users_teachers[login_t] == password_t:
        print("Zalogowano pomyślnie na koncie nauczyciela")
        platform_teacher()

    else:
        print("Nieprawidłowe dane logowania")
        program_main()


def logowanie_ucznia():
    ("______________________________________________________________")
    login_s = input("Podaj swój login: ")
    password_s = input("Podj swoje hasło: ")
    if login_s in users_students.keys() and users_students[login_s] == password_s:
        print("Zalogowano pomyślnie na koncie ucznia")
        platform_student()
    else:
        print("Nieprawidłowe dane logowania")
        program_main()


def logowanie_rodzica():
    ("______________________________________________________________")
    login_p = input("Utwórz login: ")
    password_p = input("Utwórz hasło: ")
    if login_p in users_parents.keys() and users_parents[login_p] == password_p:
        print("Zalogowano pomyślnie na koncie rodzica")
        platform_parent()
    else:
        print("Nieprawidłowe dane logowania")
# _______________________________________________________________________________________________________
# Definicje rejestrowania nauczyciela, ucznia, rodzica


def rejestrowanie_nauczyciela():
    print("______________________________________________________________")
    login = input("Utwórz login: ")
    password1 = input("Utwórz hasło: ")
    password2 = input("Powtórz hasło: ")

    if not len(login) > 1:
        raise ValueError("Login musi mieć więcej niż 5 znaków")

    if not len(password1) > 1:
        raise ValueError("Hasło musi mieć więcej niż 6 znaków")
    if not password1 == password2:
        raise ValueError("Hasła muszą być takie same")

    print("Zaakceptowano dane nauczyciela")
    users_teachers[login] = password1
    print(users_teachers)


def rejestrowanie_ucznia():
    ("______________________________________________________________")
    login = input("Utwórz login: ")
    password1 = input("Utwórz hasło: ")
    password2 = input("Powtórz hasło: ")

    if len(login) < 1:
        print("Login musi składać się conajmniej z 6 liter")
    if len(password1) < 1:
        print("Hasło musi składać się conajmniej z 6 znaków")
    if len(login) > 1 and len(password1) > 1 and password1 == password2:
        print("Zaakceptowano dane ucznia")
        users_students[login] = password1
        baza_ocen[login] = []
        print(users_students)
        platform_teacher()


def rejestrowanie_rodzica():
    ("______________________________________________________________")
    login = input("Utwórz login: ")
    password1 = input("Utwórz hasło: ")
    password2 = input("Powtórz hasło: ")

    if not len(login) > 1:
        raise ValueError("Login musi mieć więcej niż 5 znaków")

    if not len(password1) > 1:
        raise ValueError("Hasło musi mieć więcej niż 6 znaków")
    if not password1 == password2:
        raise ValueError("Hasła muszą być takie same")

    print("Zaakceptowano dane rodzica")
    users_parents[login] = password1
    print(users_parents)
    platform_teacher()
# ____________________________________________________________________________________________________
# Funkcja dodawania ocen


def dodawanie_oceny():
    print("Lista uczniów w bazie")

    for i in users_students:
        print(i)
        elect_s = input("Podaj imię ucznia: ")
        mark_in = int(input("Podaj ocenę: "))
        if elect_s in baza_ocen:
            lista_ocen.append(mark_in)
            baza_ocen[elect_s] = lista_ocen
            print("DODANA OCENA")
            print(baza_ocen)
            platform_teacher()

# ___________________________________________________________________________________________________________________________
# Funkcja publikowania komunikatów na tablicy


def publikowanie_komunikatów():
    komunikat = input(
        "Wpisz treść komunikatu i kliknij enter, aby go opubikować na tablicy: ")
    import datetime
    data = datetime.date.today()
    tablica_komunikatów[data] = komunikat
    print("______________________________________________________________")
    print(tablica_komunikatów)
    print("______________________________________________________________")
# _________________________________________________________________________________________________________________________________________
# Definicje zmiany danych logowania dla nauczycieli, uczniów, rodziców


def zmiana_danych_logowania_teachers():
    login_zmiana_hasla = input("Podaj swój login: ")
    if login_zmiana_hasla in users_teachers:

        print("Jesteś zarejestrowany w bazie")
        old_password = input("Podaj obecne hasło: ")
        if login_zmiana_hasla in users_teachers.keys() and users_teachers[login_zmiana_hasla] == old_password:
            new_password = input("Podaj nowe hasło: ")
            users_teachers[login_zmiana_hasla] = new_password
            print(users_teachers)
        else:
            print("Nie zostałeś zarejestrowany w bazie")


def zmiana_danych_logowania_students():
    login_zmiana_hasla = input("Podaj swój login: ")
    if login_zmiana_hasla in users_students:

        print("Jesteś zarejestrowany w bazie")
        old_password = input("Podaj obecne hasło: ")
        if login_zmiana_hasla in users_teachers.keys() and users_teachers[login_zmiana_hasla] == old_password:
            new_password = input("Podaj nowe hasło: ")
            users_teachers[login_zmiana_hasla] = new_password
            print(users_teachers)
        else:
            print("Nie zostałeś zarejestrowany w bazie")


def zmiana_danych_logowania_parents():
    login_zmiana_hasla = input("Podaj swój login: ")
    if login_zmiana_hasla in users_parents:

        print("Jesteś zarejestrowany w bazie")
        old_password = input("Podaj obecne hasło: ")
        if login_zmiana_hasla in users_teachers.keys() and users_teachers[login_zmiana_hasla] == old_password:
            new_password = input("Podaj nowe hasło: ")
            users_teachers[login_zmiana_hasla] = new_password
            print(users_teachers)
        else:
            print("Nie zostałeś zarejestrowany w bazie")
# ________________________________________________________________________________________________________________________________
# Platrormy komunikatów nauczyciela, ucznia, rodzica


def platform_main():

    print("______________________________________________________________")
    print("DZIENNIK WIRTUALNY UCZNIA")
    print("    Menu użytkownika     ")
    print("1.Zarejestruj konto nauczyciela")
    print("2.Zaloguj się jako nauczyciel")
    print("3.Zaloguj się jako uczeń")
    print("4.Zaloguj sie jako rodzic")
    print("5.Wyjdź z programu")
    print("______________________________________________________________")


def platform_teacher():
    print("______________________________________________________________")
    print("PLATFORMA NAUCZYCIELA")
    print("    PANEL OPCJI      ")
    print("Opcje dostępne w menu: ")
    print("1.Dodaj ucznia do bazy.")
    print("2.Wybierz ucznia i dodaj ocenę do bazy")
    print("3.Wyświetl bazę ocen")
    print("4.Wyświetl w tablicę komunikatów i publikuj wpisy")
    print("5.Zmień hasło")
    print("6.Wyloguj się")
    print("______________________________________________________________")


def platform_student():
    print("_______________________________________________________________")
    print("PLATFORMA UCZNIA")
    print(" PANEL OPCJI   ")
    print("Opcje dostępne w menu: ")
    print("1.Wyświetl oceny")
    print("2.Wyswietl tablicę komunikatów od nauczyciela")
    print("3.Zmień hasło")
    print("4.Wyloguj")
    print("_______________________________________________________________")


def platfom_parent():
    print("_______________________________________________________________")
    print("PLATFORMA RODZICA")
    print("  PANEL OPCJI    ")
    print("Opcje dostępne w menu: ")
    print("1.Wyświetl oceny")
    print("2.Wyswietl tablicę komunikatów od nauczyciela")
    print("3.Zmień hasło")
    print("4.Wyloguj")
    print("_______________________________________________________________")
# ______________________________________________________________________________________________________
# Program głównyn łączący definicje


def program_main():
    while True:
        platform_main()
        option = input("Podaj wybraną opcję: ")
        if option == "1":
            rejestrowanie_nauczyciela()

        elif option == '2':
            logowanie_nauczyciela()

            while True:

                option = input("Podaj wybraną opcję: ")
                if option == "1":
                    rejestrowanie_ucznia()
                if option == "2":
                    dodawanie_oceny()
                if option == "3":
                    print(baza_ocen.items())
                    platform_teacher()
                if option == "4":
                    publikowanie_komunikatów()
                    print("Tablica komunikatów")
                if option == "5":
                    zmiana_danych_logowania_teachers()
                if option == "6":
                    program_main()

        elif option == "3":
            logowanie_ucznia()
            while True:

                option2 = input("Podaj wybraną opcję: ")
                if option2 == "1":
                    print("Poniżej dostępna jest lista twoich ocen")
                    print(baza_ocen)
                if option2 == "2":
                    print(tablica_komunikatów.items())
                if option2 == "3":
                    zmiana_danych_logowania()
                if option2 == "4":
                    program_main()

        elif option == "4":
            logowanie_rodzica()
            while True:

                option3 = input("Podaj wybraną opcję: ")
                if option3 == "1":
                    print("Poniżej dostępna jest lista twoich ocen")
                    print(baza_ocen)
                if option3 == "2":
                    print("Poniżej dostępna jest tablica komunikatów")
                    print(tablica_komunikatów)
                if option3 == "3":
                    zmiana_danych_logowania()
                if option3 == "4":
                    program_main()

                # if option =="2":

        # else:
                #print("Niepoprawne dane logowania")

    # elif option == '3':
        # zmiana_danych_logowania()

        # platform()


program_main()

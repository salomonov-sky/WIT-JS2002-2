from pprint import pprint
from numberapp import register, login, get_users,get_logs,get_number, user, log

#Ćw_1

conn = sqlite3.connect("numberapp.db")
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users(username, password, requests_count)')
cursor.execute('CREATE TABLE IF NOT EXISTS logs(username, date, type_param, number_param)')
conn.commit()
conn.close()


user = False

while True:
    if not user:
        print('1. Zarejestruj się')
        print('2. Zaloguj się')
        print('4. Wyjdź z programu')
        option = input('Podaj opcję: ')

        if option == '1':
            register()
        elif option == '2':
            user = login()
        elif option == '4':
            break

    else:
        print('1. Wykonaj zapytanie')
        print('2. Zobacz logi')
        print('3. Wyświetl wszystkich użytkowników')
        print('4. Wyjdź z programu')
        option = input('Podaj opcję: ')

        if option == '1':
            get_number()
        elif option == '2':
            get_logs()
        elif option == '3':
            get_users()
        elif option == '4':
            break
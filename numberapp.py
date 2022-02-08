import sqlite3
from pprint import pprint
import requests

requests_count=1
def register():
    username=input("Podaj nazwę użytkownika; ")
    password=input("Podaj hasło: ")
    connection = sqlite3.connect("numberapp.db")
    cursor = connection.cursor()
    cursor.excecute("INSERT INTO users VALUES (?,?,?), (username, password, request_count"))
    connection.commit()
    connection.close()

def login():
    username1=input("Podaj nazwę użytkownika: ")
    password1=input("Podaj hasło: ")
    connection1 = sqlite3.connect("numberapp.db")
    cursor = connection1.cursor()
    queryset=cursor.execute("SELECT * from users")
    users=queryset.fetchall()
    connection1.close()
    user_objects=[]
    for user in users:
        user_objects.append(User(user[0], user[1],""))
    
    for user in user_objects:
        if user.username==username1 and user.password == password1:
            return user
        return False
class user:
    def __init__(self, username, password, request_count):
        self.username = username
        self.password = password
        self.request_count = request_count

class log:
    def __init__(self,username, date, type, type_param, number_param):
        self.username = username
        self.date = date
        self.type_param = type_param
        self.number_param = number_param

    
def get_number():
    global requests_count
    type = input('Input type(trivia, math, date, year, default: trivia): ')
    number = input('Input number(int or "random"(if the type= date, you can use month/day format)): ')
    try:
        response = requests.get(f'http://numbersapi.com/{number}/{type}')
        data = response.json()
        pprint(data)
    except:
        print("Failed")
        
    finally:
        connection = sqlite3.connect('numberapp.db')
        cursor = connection.cursor()
        queryset = cursor.execute('SELECT * FROM users')
        data = queryset.fetchall()

        for i in data:
            print(i)

        cursor.execute('UPDATE users SET requests_count = ? ',(requests_count,))
        cursor.execute('UPDATE logs SET type_param = ? ,number_param = ?',(type,number))
        requests_count += 1
        connection.commit()
        return requests_count
def get_logs():
    
def get_users():
    



        









    
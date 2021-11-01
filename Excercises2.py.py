print("Ćw-1")
lista = [1,2,3,4,5]
odwrocona_lista = lista[::-1]
print("odwrocona_lista =", odwrocona_lista)


print("Ćw-2")
lista = [1,2,3,4,5]
y = (max(lista))
z = 0

while z <= y:
    z +=1
    if y-z == 1:
        x = [z, y]
        print("lista_max =", (x))


print("Ćw-3")
lista1 = []
lista2 = []
x=2
y=-1
for x in range (2, 13):
    x = x+1
    lista1.append(x)
    if len(lista1)==11:
        print("lista1=",lista1)

while y <= 10:
    y = y + 1
    lista2.append(y)
    if len(lista2)==11:
        print("lista2=",lista2)


print("Ćw-4")
dane_logowania = {'Admin': '1234'} 
authenticated=False
for key,value in dane_logowania.items():
    a = key
    b = value
while not authenticated:
    _username_=input("Podaj nazwę użytkownika: ")
    _password_=input("Podaj hasło: ")
    if _username_ == a and _password_ == b :
        print("Logowanie poprawne")
        authenticated = True
    else:
        print("Niepoprawne dane, wprowadź dane ponownie")


print("Ćw-5")
lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
lista3 = [1,2,2,3,3,4,5]
set1 = set(lista1)
set2 = set(lista2)
set3 = set(lista3)

if set1.issubset(set2) and set2.issubset(set1) and set1.issubset(set3) and set2.issubset(set3) and set3.issubset(set2) and set3.issubset(set1) and len(set1.difference(set3)) == 0 :
    print("Wszystie listy zawierają te same elementy, lista3 zawiera dublikaty")
        

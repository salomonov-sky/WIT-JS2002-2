def Czy_na_liście():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    is_it = input("Podaj element: ")
    is_it = int(is_it)
    if is_it in lista:
        print("Element jest na liście")
    else:
        print("Elementu nie ma na liście")


Czy_na_liście()

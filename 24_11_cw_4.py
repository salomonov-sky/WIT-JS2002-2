def Ile_znaków():
    wyraz = input("Podaj ciąg znaków: ")
    wyraz = str(wyraz)
    if not len(wyraz) == 8:
        raise ValueError("Wyraz nie ma 8 znaków")
    else:
        print("Wyraz ma 8 znaków")


Ile_znaków()

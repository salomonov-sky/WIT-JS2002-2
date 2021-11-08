print("funkcja1")


def convert_string_to_number():
    print("output=", int(x))


x = input("Podaj cyfrę lub liczbę: ")
convert_string_to_number()

print("funkcja2")


def find_min():
    print("Output=", min(lista))


lista = []

lista.extend(input("Input: "))
print("Input = ", lista)
find_min()


print("funkcja3")


def print_list():
    print("Output")
    for i in lista:
        print(i)


lista = []
lista.extend(input("Input: "))
print_list()


print("funkcja4")


def print_dict():
    for key, value in dict.items():
        print(key, value)


dict = {"a": 1, "b": 2, "c": 3}
print_dict()

print("funkcja5")


def get_length():
    print("get_length: ", len(x))


x = input("Podaj wyraz: ")
get_length()

print("funkcja6")


def remove_outer_characters():
    print("remove_outer_characters: ", x[1:-1])


x = input("Podaj wyraz: ")
remove_outer_characters()

print("funkcja7")


def count_chars(x):
    return {i: x.count(i) for i in set(x)}


print(count_chars(input("Podaj wyraz: ")))

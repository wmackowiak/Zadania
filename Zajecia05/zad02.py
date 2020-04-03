# Napisz funkcję, która pyta użytkowników o pary książka + ocena i zapisuje je w programie.
# Napisz funkcję, która zapyta o numer książki i wyświetli książkę wraz z oceną.
# W prosty sposób obsłuży błąd użytkownika - użytkownik zapyta o numer w bazie, który nie istnieje.

def add_books_to_library():

    books =[]
    for k in range(counter):
        title = input("Podaj tytuł książki: ")
        grade = int(input("Podaj ocenę ksążki 1-10: "))
        books.append((title, grade))
        print("---------------------")
    return books

def show_book():
    nr = int(intut("Podaj numer książki do wyświetlenia:"))
    index = nr - 1
    if index >= len(books):
        print("Nie masz tyle książek")
    else:
        print(f"Twoja książka to {books[indeks]}")


# counter = int(input("Ile ksążek chcesz dodać?"))
# library = add_books_to_library(counter)
# print(library)
# show_book(library)

print(show_book.__doc__)
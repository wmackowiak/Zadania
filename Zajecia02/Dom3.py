"""
    Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
    Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
    Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
    Połącz dane w jeden ciąg book za pomocą spacji
    Policz liczbę wszystkich znaków w napisie book
"""

tytul = input("Podaj tytuł ksążki: ")
autor =  input("Podaj nazwisko autora: ")
str = input("Poldaj liczbę stron: ")
print(tytul.isalpha())
print(autor.isalpha())
print(str.isnumeric())

book = tytul.title()+" "+autor.title()+" " + str
print(book)
print(len(book))
#Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

znaki = input("Wprowadź ciąg znaków ")
if len(znaki) > 5:
    #print(len(znaki))
    for litera in znaki:
        if litera == 'a':
            print(litera.replace("a", "z"),end= " ")
        else:
            print(litera,end=" ")
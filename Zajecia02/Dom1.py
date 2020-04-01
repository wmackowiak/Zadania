#Stwórz zmienną przechowującą wyraz o długości nieparzystej większej
# niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

txt = input("Podaj wyraz o długości nieparzystej większej niż 7")
dlugosc = len(txt)
parzysta = len(txt)/2
#print("znaków:",dlugosc)
#print("dzielenie:",parzysta)
#print("modulo:",len(txt)%2)

if dlugosc >= 7:
    if (len(txt) % 2) != 0:

        nowy = txt[int(parzysta) - 1] + txt[int(parzysta)] + txt[int(parzysta) + 1]
        print(nowy)

        #print("Wpisany wyraz posiada nieparzystą liczbę znaków")
    else:
        print("Twój ciąg znaków ma parzystą liczbę znaków")

else:
    print("Zbyt krótki ciąg znaków")



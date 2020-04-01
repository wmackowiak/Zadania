#Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

txt = input("Podaj teks o dł nieparzystej większej niż 7")
center = len(txt)//2
nowy_txt = txt[center -1] + txt[center] + txt[center +1]
print(nowy_txt)



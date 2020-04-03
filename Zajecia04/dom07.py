# 9▹ 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach. Wyświetl
# # najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając
# # od dużej litery)

# lista = []
# for uzytkownik in range(3):
#     for i in range(3):
#         przedmiot = input("Podaj przedmiot: ")
#         lista.append(przedmiot.lower())
#     print(f"Twój wybór: {lista}")
#     lista = []
# print("**********")

lista = []
for uzytkownik in range(3):
    for i in range(3):
        przedmiot = input("Podaj przedmiot: ")
        lista.append(przedmiot.lower())
    print("**********")
print(lista)

print("**********")
unikatowe = {}
for w in lista:
    if w in unikatowe:
        # worlds_in_poem[w] = worlds_in_poem[w] + 1
        unikatowe[w] += 1
    else:
        unikatowe[w] = 1

for przedm, number in unikatowe.items():
    print(f"{przedm}:{number}")






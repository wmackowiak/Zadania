# Poprzednie zadanie było dość radykalne dla użytkownika. Na pewno lepiej by było dać użytkownikowi drugą szansę,
# aby mógł poprawić swój błąd. Fajnie by było, gdyby użytkownik mógł próbować wpisywać litery aż do skutku. Proszę
# napisać kod, w którym użytkownik będzie mógł wpisywać litery aż uda mu się wpisać n albo c.

for i in range(30):
    litera = input("Wpisz literę n lub c: ")

    if litera =='n' or litera == 'c':
        print("Dziękuję!")
        break
    else:
        print("Spróbuj jeszcze raz!")
# Proszę, używając pętli for, napisać kod, który poprosi o wpisanie sześciu wartości. Po wpisaniu tych wartości
# program ma podsumować ile razy wprowadzona została wartość 5.
#
# Wprowadź dowolną liczbę od 1 do 10: 2
# Wprowadź dowolną liczbę od 1 do 10: 3
# Wprowadź dowolną liczbę od 1 do 10: 5
# Wprowadź dowolną liczbę od 1 do 10: 5
# Wprowadź dowolną liczbę od 1 do 10: 5
# Użytkownik wybrał 3 razy liczbę 5.

suma = 0
for i in range(6):
    liczba = input("Proszę podać liczbę: ")
    if liczba == '5':
            suma += 1
print("Użytkownik wybrał " + str(suma) + " razy liczbę 5.")



# Proszę, używając pętli for, napisać kod, który poprosi o wpisanie trzech wartości. Po wpisaniu tych wartości mają
# być one podsumowane.

# Wprowadź wartość:
# 4
# Wprowadź wartość:
# 2
# Wprowadź wartość:
# 2
# Suma wpisanych wartości to: 8

suma = 0
for i in range(3):
    liczba = input("Wprowadz wartość: ")
    suma += int(liczba)
print("Suma wpisanych wartości to: " + str(suma))





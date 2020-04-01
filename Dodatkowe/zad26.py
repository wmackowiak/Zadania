# Proszę napisać program wykorzystujący pętle while, który będzie sumował kolejne liczby całkowite w ciągu.
# Użytkownik musi wpisać liczbę kończącą ciąg, np. 3. Program obliczy: 1+2+3 = 6.
#
# Wprowadź wartość: 21
# Suma liczb wynosi: 231

n = input("Wprowadź wartość: ")
suma = 0
i = 1
while i <= int(n):
    suma = suma + i
    i = i + 1
print("Suma liczb wynosi: " + str(suma))
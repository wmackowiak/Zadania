#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = 'abrakadabra'
s2 = 'czarymary'
dlugosc = len(s1)
print(dlugosc)
polowa = int(len(s1)/2)
print(polowa)
s3 = s1[:polowa] + s2 + s1[polowa:]
print(s3)

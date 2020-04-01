# Proszę napisać funkcję witającą, opartą na pętli for. Funkcja ma działać przy podstawieniu do każdej listy.
# W przykładzie są dwie listy: ['Wojciech','Tomasz','Adrian'] i ['szop','zając','krowa'].
#
# Wojciech Tomasz Adrian
# Witamy w naszym zespole!
#
# szop zając krowa
# Witamy w naszym zespole!

a = ['Wojciech','Tomasz','Adrian']
b = ['szop','zając','krowa']

for imie in b:
    print(imie,end=" ")
print()
print("Witamy w naszym zespole!")



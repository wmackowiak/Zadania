#Set

#diskard()
#remove()

#3▹ Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki, a oraz
# nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

krt1 = ("a","b","c","d")
krt2 = (1,1,3,4,5,6,1,1,1,1)
result = list(krt1[::2] + krt2[1::2])
result = set(result)
print(result)
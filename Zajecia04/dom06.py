# 6▹ Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.
#
days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

for key in days.keys():
    lista1 = list(set(days.keys()))


for value in days.values():
    lista2 = list(set(days.values()))

print(lista1)
print(lista2)




# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
"""Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

# Zadbaj o sposób wyświetlania np.:
#     szybko : 5
#     zbudź : 1

# print("***")
# txt = 'Szybko, zbudź się, szybko, wstawaj Szybko, szybko, stygnie kawa Szybko, zęby myj i ręce'
# new_txt = txt.replace(",","").lower().split(" ")
# print(new_txt)
# print(type(new_txt))
# print(set(new_txt))
# print(type(set(new_txt)))
# print(list(set(new_txt)))
# print(type(list(set(new_txt))))
#
# for slowo in set(new_txt):
#     print(slowo)
#
#
#
# print("***")
#
# txt = 'Szybko, zbudź się, szybko, wstawaj Szybko, szybko, stygnie kawa Szybko, zęby myj i ręce'
# txt_bz = txt.replace(",","")
# print(txt_bz.lower())
# print("-------------")
# dictionary = {}
# l1 = list(txt_bz.lower().split(" "))
# for slowo in l1:
#     if slowo in
#     slowo +=1



# print("-------------")
# print(set(txt_bz.lower().split(" ")))
# nowa_lista = list(set(txt_bz.lower().split(" ")))
# print(nowa_lista)
# for unik in nowa_lista:
#     print(unik,slowo, ": ",l1.count(slowo))


# i = 0
# for x in nowa_lista:
#     print(nowa_lista.count(x))
#     # i+=1
#     # print(x,i)

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem = poem.lower()
poem = poem.replace(",","")
world_list = poem.split()
print(poem)
worlds_in_poem = {}
for w in world_list:
    if w in worlds_in_poem:
        # worlds_in_poem[w] = worlds_in_poem[w] + 1
        worlds_in_poem[w] += 1
    else:
        worlds_in_poem[w] = 1

for world, number in worlds_in_poem.items():
    print(f"{world}:{number}")


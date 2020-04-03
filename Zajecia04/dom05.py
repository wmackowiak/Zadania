# Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
unikalne = set(example_list)
krotka = tuple(unikalne.copy())

print(type(krotka))
max(krotka)
min(krotka)
print(krotka)
print(f"max to {max(krotka)}, min to {min(krotka)}")




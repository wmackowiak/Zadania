#Policz elementy na liście, dopóki element nie będzie krotką.

numbers = [1, 2, 3, (10, 20), 4, 5]
counter = 0
for n in numbers:

# * isinstance(obiekt, typ_lub_klasa) -- sprawdza czy obiekt jest instancją typu/klasy typ_lub_klasa lub dowolnego
# typu/klasy dziedziczącego z typ_lub_klasa,

  if isinstance(n, tuple):
      break
  counter += 1
print('Wynik:', counter)
#Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

liczba1 = input("Podaj liczbę: ")
liczba2 = input("Podaj liczbę: ")
suma = int(liczba1) + int(liczba2)
if suma > 100:
    print(suma)
else:
    print("Koniec")
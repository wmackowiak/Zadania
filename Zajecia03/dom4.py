# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl
# komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

liczba_uzytkownika = input("Podaj liczbę z przedziału od 1 do 100: ")
moja_liczba = '45'

if liczba_uzytkownika == moja_liczba:
    print("Gratulacje!")
else:
    print("Pudło!")
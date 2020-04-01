# 8▹ Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
#     Program zacznie ze stworzonym słownikiem o trzech kluczach:
#             marka (str)
#             model (str)
#             rocznik (int)
#     Wypisze ten słownik na ekran (bez żadnego formatowania)
#     Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
#         “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
#     Jeśli nie spełnia powyższego warunku, wypisze komunikat:
#         “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
#     Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam
#     również zmienia swoje zachowanie.

slownik = {'marka': 'Ford','model': 'T','rocznik': 1920}
# marka = str(input("Podaj markę samochodu: "))
# model = str(input("Podaj model samochodu: "))
# rocznik = int(input("Podaj rok produkcji: "))
print(slownik)


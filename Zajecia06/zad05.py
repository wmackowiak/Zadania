# Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych. Sprawdź dla każdej kart jej typ.
# Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.

def is_card_number(number):
    return number.isdecimal() and len(number) in (13, 15, 16)
def starts_with_correct_digits(number):
    if 51 <= int(number[0:2]) <= 55:
        return True
    elif 2221 <= int(number[0:4]) <= 2720:
        return True
    else:
        return False

with open('karty.txt', 'r', encoding='utf-8') as fopen:
    cards = fopen.read()
    cards = cards.split()
for nr_card in cards:

nr_card = input("Podaj nr karty: ")

if is_card_number(nr_card):
    if len(nr_card) in [13,16] and nr_card[0] == '4':
        print("To jest Visa")
    elif len(nr_card) == 16 and starts_with_correct_digits(nr_card):
        print("To jest Mastercard")
    elif len(nr_card) == 15 and (nr_card[0:2] in ['34','37']):
        print("To jest American Express")
    else:
        print("Nie znam typu karty")
else:
    print("To nie jest nr karty")
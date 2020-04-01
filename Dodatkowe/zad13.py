# Proszę napisać kod, który będzie prosił użytkownika o napisanie liter n lub c. Jeżeli użytkownik wpiszę właściwą
# literę, program ma wygenerować komunikat: „Dziękuję!”. Jeżeli użytkownik wpisze złą literę, program ma mu zwrócić uwagę.
# W tym zadaniu nie trzeba tworzyć pętli.

litera = input("Wpisz literę n lub c: ")
if litera == 'n':
    print('Dziękuję!')
elif litera == 'c':
    print('Dziękuję!')
else:
    print("Spróbuj raz jeszcze")

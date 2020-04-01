#W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

txt = input("Podaj dowolny ciąg: ")

char_lower = 0
char_upper = 0
digit = 0
symbols = 0
for l in txt:
    if l.islower():
        char_lower +=1
    if l.isupper():
        char_upper +=1
    if l.isdecimal():
        digit +=1
    if l.isalnum():
        symbols +=1

print({char_lower},{char_upper},{digit},{symbols})
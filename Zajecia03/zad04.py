#Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
# W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

ocena1 = int(input("Jaka jest Twoja ocena ksążki?"))
ocena2 = int(input("Jaka jest Twoja ocena ksążki?"))
ocena3 = int(input("Jaka jest Twoja ocena ksążki?"))

srednia = round(float((ocena1 + ocena2 + ocena3) / 3),0)
print(srednia)

if srednia > 7:
    print("bardzo dobry")
elif srednia >=5 and srednia <=7:
    print("przeciętna")
else:
    print("nie warta uwagi")


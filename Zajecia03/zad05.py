#Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

waga = float(input("Twoja waga w kg :"))
wzrost = float(input("Twój wzrost w m: "))

bmi = waga / wzrost ** 2
print("Moje BMI to: :", round(bmi, 2))

if bmi < 18:
    print("niedowaga")
elif bmi < 25:
    print("waga normalna")
elif bmi < 30:
    print("nadwaga")
else:
    print("otyłość")



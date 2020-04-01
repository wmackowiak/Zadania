# Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika oraz
# zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

# #Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku:
# # niedowaga / waga normalna / nadwaga / otyłość.
#
# waga = float(input("Twoja waga w kg :"))
# wzrost = float(input("Twój wzrost w m: "))
#
# bmi = waga / wzrost ** 2
# print("Moje BMI to: :", round(bmi, 2))
#
# if bmi < 18:
#     print("niedowaga")
# elif bmi < 25:
#     print("waga normalna")
# elif bmi < 30:
#     print("nadwaga")
# else:
#     print("otyłość")


# funkcja obliczająca bmi <-- waga, wzrost
def calculate_bmi(weight,height):
    return weight/height **2

# funkcja podająca wartość
def get_state(bmi):
    if bmi < 18:
        print("niedowaga")
    elif bmi < 25:
        print("waga normalna")
    elif bmi < 30:
        print("nadwaga")
    else:
        print("otyłość")

# reszta kodu

# podaj wagę i wrost
weight = float(input("Podaj wagę w kg: "))
height = float(input("Podaj wzrost w m: "))

# wyślij wagę i wzrost do funkcji obliczjącej
result_bmi = calculate_bmi(weight, height)
get_state(result_bmi)
# dowiedz się jaki jest stan twojego bmi na podstawie wyniku
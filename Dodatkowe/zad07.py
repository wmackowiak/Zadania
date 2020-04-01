# Proszę znaleźć wszystkie liczby ze przedziału (1,20), które dzielą się bez reszty przez 3.

for i in range(1,20):
    if i % 3 == 0:
        print(i)
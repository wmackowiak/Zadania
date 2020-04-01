# Proszę za pomocą pętli while zbudować kalkulator liczący wartość silnia z liczb całkowitych.
#
# Wprowadź wartość: 3
# Silnia wynosi:  6
#
# 0! = 1
# 1! = 1
# 2! = 2*1 = 2
# 3! = 3*2*1 = 6
# 4! = 1*2*3*4 = 24

liczba = int(input("Wprowadź wartość: "))

a=1
if liczba == 0:
    print("Silnia wynosi: 1")
else:
    while liczba >= 1:
        a = liczba * a
        liczba = liczba -1
    print("Silnia wynosi: ",a)



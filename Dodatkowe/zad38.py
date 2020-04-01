# Proszę za pomocą pętli for wygenerować ciąg liczb od 10 do 40, które nie są podzielne przez 5, 3 oraz 2.
# Proszę zdefiniować tą pętle jako funkcję.
#
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37

for i in range(10,40):
    if i%5 == 0:
        continue
    if i%3 == 0:
        continue
    if i%2 == 0:
        continue
    print(i)



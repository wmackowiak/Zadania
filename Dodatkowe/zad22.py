# Używając pętli for-if proszę wypisać liczby od 1 do 10, następnie tak skonstruować instrukcją if, aby z listy
# zniknęły liczby: 9, 8 i 3.
#
# 1
# 2
# 4
# 5
# 7
# 10

for i in range(1,11):
    if (i != 3 and i != 8 and i != 9):
        print(i)

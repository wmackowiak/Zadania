# Proszę za pomocą pętli for, z listy: a = ('ARA','BereKA','GONabEACH') wyświetlić wyrazy wraz z ich numerami porządkowymi.
#
# To są wyrazy do wyboru:
# 1 ARA
# 2 BereKA
# 3 GONabEACH

a = ['ARA','BereKA','GONabEACH']
for x in range((len(a)+1)):
    print(x+1, a[x])

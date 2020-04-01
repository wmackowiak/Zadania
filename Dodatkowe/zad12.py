# Proszę używając pętli for, połączyć dwie listy według poniższego wzoru.
#
# lista1 = ["KKKK", "GGGG", "HHHH"]
# lista2 = ["563-12", "363-AB"]
#
# KKKK 563-12
# KKKK 363-AB
# -----------
# GGGG 563-12
# GGGG 363-AB
# -----------
# HHHH 563-12
# HHHH 363-AB
# -----------

lista1 = ["KKKK", "GGGG", "HHHH"]
lista2 = ["563-12", "363-AB"]
for a in lista1:
    for b in lista2:
        print(a+" "+b)
# Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi). Następnie rozpakuj tę krotkę
# na pojedyńcze zmienne. Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np. “Mój pies, rasy
# border collie wabi się Dyzio”.

krotka = ('pies','jamnik','Reksio')
(rodzaj, rasa, ksywa) = krotka
print(ksywa)
print(rasa)
print(rodzaj)

print(f"Mój {rodzaj}, rasy {rasa} wabi się {ksywa}.")
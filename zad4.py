def sprawdz_sume(liczba1, liczba2, liczba3):
    suma_dwoch_pierwszych = liczba1 + liczba2
    return suma_dwoch_pierwszych >= liczba3


arg1 = 5
arg2 = 8
arg3 = 12
wynik_sprawdzenia = sprawdz_sume(arg1, arg2, arg3)

print(wynik_sprawdzenia)

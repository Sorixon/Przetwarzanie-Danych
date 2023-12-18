def sprawdz_wartosc(lista, szukana_wartosc):
    return szukana_wartosc in lista


moja_lista = [1, 3, 5, 7, 9]
wartosc_do_sprawdzenia = 5
wynik_sprawdzenia = sprawdz_wartosc(moja_lista, wartosc_do_sprawdzenia)

print(wynik_sprawdzenia)

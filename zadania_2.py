def pomnoz_przez_2_for(lista_liczb):
    wynik = []
    for liczba in lista_liczb:
        wynik.append(liczba * 2)
    return wynik


lista_liczb = [1, 2, 3, 4, 5]
wynik_for = pomnoz_przez_2_for(lista_liczb)
print(wynik_for)

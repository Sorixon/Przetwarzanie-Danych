
def polacz_i_przetworz(lista1, lista2):
    lista_polaczona = lista1 + lista2
    lista_unikalna = list(set(lista_polaczona))
    lista_wynikowa = [element**3 for element in lista_unikalna]

    return lista_wynikowa

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
wynik = polacz_i_przetworz(lista1, lista2)

print(wynik)
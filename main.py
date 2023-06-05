import numpy as np


# Printowanie macierzy z liczbami na lewo

def lewo(wiersze):
    szerokosc = [max(len(str(wiersz[i])) for wiersz in wiersze) for i in range(len(wiersze[0]))]
    zmienione_wiersze = []
    for wiersz in wiersze:
        zmieniony_wiersz = '[{}]'.format('  ,  '.join(str(val).ljust(width) for val, width in zip(wiersz, szerokosc)))
        zmienione_wiersze.append(zmieniony_wiersz)
    return '\n'.join(zmienione_wiersze)


# wiersze = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
# wyjscie = lewo(wiersze)
# print(wyjscie)

# Printowanie macierzy z liczbami na prawo

def porzadkowanie_na_prawo(wiersze):
    macierz = np.matrix(wiersze)
    return str(macierz)


print(porzadkowanie_na_prawo([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]))

# Test prawo

input = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
oczekiwany_output = '[[   1    2   10  150]\n [  10    2 1000    2]\n [   1  120    1 1000]]'
assert porzadkowanie_na_prawo(input) == oczekiwany_output

# Test lewo

input1 = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
output1 = '[1   ,  2    ,  10    ,  150 ]\n[10  ,  2    ,  1000  ,  2   ]\n[1   ,  120  ,  1     ,  1000]'
assert lewo(input1) == output1

def lewo(wiersze):
    szerokosc = [max(len(str(wiersz[i])) for wiersz in wiersze) for i in range(len(wiersze[0]))]
    zmienione_wiersze = []
    for wiersz in wiersze:
        zmieniony_wiersz = '[{}]'.format('  ,  '.join(str(val).ljust(width) for val, width in zip(wiersz, szerokosc)))
        zmienione_wiersze.append(zmieniony_wiersz)
    return '\n'.join(zmienione_wiersze)
wiersze = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
wyjscie = lewo(wiersze)
print(wyjscie)

# Printowanie macierzy z liczbami na prawo

def porzadkowanie_na_prawo(wiersze):
    import numpy as np
    macierz = np.matrix(wiersze)
    return macierz


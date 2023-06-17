import numpy as np
import math as math


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


# print(porzadkowanie_na_prawo([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]))

# Test prawo

input = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
oczekiwany_output = '[[   1    2   10  150]\n [  10    2 1000    2]\n [   1  120    1 1000]]'
assert porzadkowanie_na_prawo(input) == oczekiwany_output

# Test lewo

input1 = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
output1 = '[1   ,  2    ,  10    ,  150 ]\n[10  ,  2    ,  1000  ,  2   ]\n[1   ,  120  ,  1     ,  1000]'
assert lewo(input1) == output1


# Wierzchołek kwadratu

def kwadrat(wierzcholki):
    x = [wierzcholek[0] for wierzcholek in wierzcholki]
    y = [wierzcholek[1] for wierzcholek in wierzcholki]

    ab = math.sqrt(((x[0] - x[1]) ** 2) + ((y[0] - y[1]) ** 2))
    ac = math.sqrt(((x[0] - x[2]) ** 2) + ((y[0] - y[2]) ** 2))

    if ab < ac:
        pozostalyx = x[0] + x[2] - x[1]
        pozostalyy = y[0] + y[2] - y[1]
    else:
        pozostalyx = x[0] + x[1] - x[2]
        pozostalyy = y[0] + y[1] - y[2]

    return [pozostalyx, pozostalyy]


kwadrat1 = [[1, 1], [2, 3], [4, 2]]
print(kwadrat(kwadrat1))

# traingle

def third_vertex(x1, y1, x2, y2):

    # calculate the distance between (x1, y1) and (x2, y2)
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # calculate the angle between the two points (x1, y1) and (x2, y2)
    angle = math.atan2(y2 - y1, x2 - x1)

    # calculate the coordinate of the first point of third vertex
    x3_1 = x1 + distance * math.cos(angle - (1 * math.pi / 3))
    y3_1 = y1 + distance * math.sin(angle - (1 * math.pi / 3))

    # calculate the coordinate of the second point of third vertex
    x3_2 = x1 + distance * math.cos(angle + (1 * math.pi / 3))
    y3_2 = y1 + distance * math.sin(angle + (1 * math.pi / 3))


    return[(x3_1, y3_1), (x3_2, y3_2)]

# Example

x1, y1 = 1, 1
x2, y2 = 2, 3

third_points = third_vertex(x1, y1, x2, y2)

for i, point in enumerate(third_points):
    print("Third vertex (number {}):".format(i+1), point)

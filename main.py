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


def test_kwadrat():
    kwadrat1 = [[1, 1], [2, 3], [4, 2]]
    result1 = kwadrat(kwadrat1)
    assert result1 == [3, 0], f"Expected [3, 0], but got {result1}"

    kwadrat2 = [[0, 0], [0, 4], [4, 4]]
    result2 = kwadrat(kwadrat2)
    assert result2 == [4, 0], f"Expected [4, 0], but got {result2}"

    kwadrat3 = [[-1, -1], [2, 2], [4, 1]]
    result3 = kwadrat(kwadrat3)
    assert result3 == [1, -2], f"Expected [1, -1], but got {result3}"

    print("All test cases pass")

test_kwadrat()

def test_third_vertex():
    x1, y1 = 1, 1
    x2, y2 = 2, 3
    result1 = third_vertex(x1, y1, x2, y2)
    expected1 = [(3.232050807568877, 1.1339745962155614), (-0.23205080756887653, 2.8660254037844393)]
    assert result1 == expected1, f"Expected {expected1}, but got {result1}"

    x3, y3 = 0, 0
    x4, y4 = 5, 0
    result2 = third_vertex(x3, y3, x4, y4)
    expected2 = [(2.5000000000000004, -4.330127018922193), (2.5000000000000004, 4.330127018922193)]
    assert result2 == expected2, f"Expected {expected2}, but got {result2}"

    x5, y5 = -2, -2
    x6, y6 = 3, 4
    result3 = third_vertex(x5, y5, x6, y6)
    expected3 = [(5.696152422706632, -3.3301270189221923), (-4.696152422706631, 5.330127018922194)]
    assert result3 == expected3, f"Expected {expected3}, but got {result3}"

    print("All test cases pass")

test_third_vertex()


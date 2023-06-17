# traingle

import math

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
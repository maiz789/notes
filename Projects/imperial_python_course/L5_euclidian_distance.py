import math
def euclidian_distance(x1, y1, x2, y2):
    pass
    xlength = x2 - x1
    ylength = y2 - y1
    hlength = math.sqrt(xlength**2 + ylength**2)
    return hlength

distance = euclidian_distance(2,3,-2,1)
expected_answer = 4.4721
epsilon = 0.0001
if(abs(distance - expected_answer) > epsilon):
    print(f"Incorrect implementation. Calculated distance is {distance}.")
else:
    print(f'Correct implementation. Calculated distance is {distance}.')
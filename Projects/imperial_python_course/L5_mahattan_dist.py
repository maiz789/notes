def manhattan_distance(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)
    #pass

def test_manhattan_distance():
    # Complete this first!
    epsilon = 0.001
    x1 = 1
    y1 = 2

    x2 = 9
    y2 = 4
    expected_answer = 10
    assert abs(manhattan_distance(x1, y1, x2, y2) - expected_answer) < epsilon, f'calculation is wrong'

test_manhattan_distance()
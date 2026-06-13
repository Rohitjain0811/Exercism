def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == 0 or b == 0 or c == 0:
        return False

    return a == b == c

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == 0 or b == 0 or c == 0:
        return False

    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return a == b or b == c or a == c


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == 0 or b == 0 or c == 0:
        return False

    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return a != b and b != c and a != c

from numpy import array as na
from numpy import polyval as pv
from numpy.linalg import solve


def sequence(n):
    result = 0
    result += 1
    result -= n
    result += pow(n, 2)
    result -= pow(n, 3)
    result += pow(n, 4)
    result -= pow(n, 5)
    result += pow(n, 6)
    result -= pow(n, 7)
    result += pow(n, 8)
    result -= pow(n, 9)
    result += pow(n, 10)
    return result


def getFitForN(N):
    a = []
    for i in range(1, N + 1):
        row = []
        for j in range(N - 1, -1, -1):
            row.append(pow(i, j))
        a.append(row)
    a = na(a)
    b = na([sequence(i) for i in range(1, N + 1)])
    coeffs = solve(a, b)
    fit = pv(coeffs, N + 1)
    return fit


print reduce(lambda x, y: x + y, [getFitForN(i) for i in range(1, 11)])

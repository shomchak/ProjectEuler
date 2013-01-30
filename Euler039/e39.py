import time

def main():
    perfect_triangles = {}
    for p in range(12, 1001, 2):
        perfect_triangles[p] = 0
        for c in range(1, int(p / 2)):
            for a in range(1, int((p - c) / 2)):
                b = p - c - a
                if c * c == a * a + b * b:
                    perfect_triangles[p] += 1
    P = 0
    T = 0
    for p, t in perfect_triangles.iteritems():
        if t > T:
            T = t
            P = p
    return P, T

start = time.time()
print main(), time.time() - start

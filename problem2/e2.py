'''
Every third term in the Fibonacci sequence is even, and this comprises all the
even terms in the sequence. We can use this to caculate the even terms directly
rather than having to test each term individually for evenness.

If the sequence starts with (odd) terms a and b, then the even term that follows
is a + b. The two new odd terms that follow, a' and b', can be defined with the
following relation

a' = a + 2b,
b' = 2a + 3b = 2a' - b.
'''


def solve():
    a, b, tot, limit = 1, 1, 0, 4000000
    while (a + b) <= limit:
        tot += a + b
        a = a + 2 * b
        b = 2 * a - b
    return tot

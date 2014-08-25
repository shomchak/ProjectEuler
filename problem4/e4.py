
def solve():
    '''
    brute force: calculate each of the 900-choose-2 products, testing each for
    palindrome-ness as it is calcualted, and keep the largest
    '''
    maximum = 0
    for m in range(100, 1000):
        for n in range(m, 1000):
            product = m * n
            if str(product) == str(product)[::-1]:
                if product > maximum:
                    maximum = product
    return maximum

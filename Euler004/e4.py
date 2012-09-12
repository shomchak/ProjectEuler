# Generate a list of products, sort them in descending order, iterate and test for palindrome-ness

def isPalindrome(n):
    if str(n) == str(n)[::-1]: return True
    else: return False
    
def genList():
    products = []
    for n in range(100, 1000):
        for m in range(n, 1000):
            products.append(n*m)
    products.sort(reverse=True)
    return products

def testList():
    for element in genList():
        if isPalindrome(element):
            print element
            break

testList()

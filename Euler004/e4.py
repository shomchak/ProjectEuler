# brute force: calculate each of the 900-choose-2 products, testing each for palindrome-ness 
# as it is calcualted, and keep the largest

def isPalindrome(n):
    if str(n) == str(n)[::-1]: return True
    else: return False
    
def main():
    max = 0
    for m in range(100, 1000):
        for n in range(m, 1000):
            if str(n) == str(n)[::-1]: 
                if m*n > max:
                    max = m*n
    print max
            
main()

def isprime(n):
    n*=1.0
    if n%2==0 and n!=2 or n%3==0 and n!=3:
        return False
    for b in range(1,int((n**0.5+1)/6.0+1)):
        if n%(6*b-1)==0:
            return False
        if n %(6*b+1)==0:
           return False
    return True

def largestprimefactor(n):
    if type(n) != int:  #test for integerness
        print n, "is not an integer."
    else:   
        for number in range(0, int(n**0.5)):    #divide by all ints
                                                #below squareroot of number
            test = int(n**0.5) - number #reverses ordering of divisors
                                        #so divisors start at
                                        #sqrt(n) and go down
            if n % test == 0:   
                if isprime(test) == True:  #checks if a divisor is prime
                    print test, "is the largest prime factor of", n
                    break
        else:   #loop didn't find a prime factor
            print n, 'is a prime number.'

entry = raw_input('Enter a number : ')
largestprimefactor(int(entry))
                
            

def getPrimes(N):
    composites = {}
    guess = 2
    while guess <= N:
        if guess in composites:
            for prime in composites[guess]:
                composites.setdefault(guess+prime,[]).append(prime)
            del composites[guess]
        else:
            yield guess
            #composites.setdefault(2*guess,[]).append(guess)
            composites[guess*guess] = [guess]
        guess += 1
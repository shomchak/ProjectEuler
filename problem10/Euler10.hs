module Euler10 where
import PrimeSieve (primes)

solve :: Integer
solve = sum $ primes 2000000

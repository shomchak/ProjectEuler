module Main where
import PrimeSieve (primes)

main = print $ show solve

solve :: Integer
solve = sum $ primes 2000000

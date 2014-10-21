module Euler7 where

solve = print $ show $ primes !! n where n = 10001

-- | A list of all primes.
primes :: [Integer]
primes = 2 : filter isPrime [3,5..]
  where isPrime n   = all (not . divides n) $ takeWhile (lt_sqrt n) primes
        divides n p = mod n p == 0
        lt_sqrt n p = p <= (floor $ sqrt $ fromIntegral n)

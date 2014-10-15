module Primes (
    primes
    , lt_sqrt
    , divides) where

-- | A list of all primes.
primes :: [Integer]
primes = 2 : filter isPrime [3,5..]
    where isPrime n = all (not . divides n) $ takeWhile (lt_sqrt n) primes

-- | Whether the square root of a number is greater than another number.
lt_sqrt :: (Integral a) => a -> a -> Bool
lt_sqrt n p = p <= (floor $ sqrt $ fromIntegral n)

-- | Whether a number is evenly divided by another number.
divides :: (Integral a) => a -> a -> Bool
divides n p = mod n p == 0


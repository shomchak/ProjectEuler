module Euler3 where

solve :: Integer
solve = solveIter the_number factors
    where the_number = 600851475143
          lt_root p  = fromIntegral p <= (sqrt $ fromIntegral the_number)
          factors    = filter (divides the_number) $ takeWhile lt_root primes

-- | Divide <n> by its prime factors until it is 1.
solveIter :: Integer -> [Integer] -> Integer
solveIter n [] = n
solveIter n (f:fs)
    | m /= 0    = solveIter n fs
    | q == 1    = f
    | otherwise = solveIter q fs
        where m = mod n f
              q = quot n f

-- | A list of all primes.
primes :: [Integer]
primes = 2 : filter prime [3,5..]
    where prime n     = all (not . divides n) $ takeWhile (lt_half n) primes
          lt_half n p = p < (quot n 2)

divides :: (Integral a) => a -> a -> Bool
divides n p = mod n p == 0


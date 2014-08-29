module Euler5 where

primeFactors :: Integer -> [Integer]
primeFactors n = primeFactorsIter n $ takeWhile (<=n) primes
    where primeFactorsIter n ps
            | n <= 1    = []
            | otherwise = let p = head ps
                              q = quot n p in
                            case divides n p of
                                True  -> p : primeFactorsIter q ps
                                False -> primeFactorsIter n $ tail ps

-- | A list of all primes.
primes :: [Integer]
primes = 2 : filter prime [3,5..]
    where prime n     = all (not . divides n) $ takeWhile (lt_half n) primes
          lt_half n p = p < (quot n 2)

divides :: (Integral a) => a -> a -> Bool
divides n p = mod n p == 0


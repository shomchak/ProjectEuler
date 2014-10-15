module Main where
import Data.List (nub, maximumBy)
import Data.Function (on)
import System.Environment (getArgs)

import Primes (primes, lt_sqrt, divides)

main :: IO ()
main = do args <- getArgs
          putStrLn $ show $ solve $ read $ args !! 0

solve :: Integer -> Integer
solve n = minMultiple [1..n]

minMultiple :: [Integer] -> Integer
minMultiple xs = foldr (*) 1 $ foldr join [] $ map primeFactors xs

join :: (Ord a) => [a] -> [a] -> [a]
join xs ys = nub (xs ++ ys) >>= longer xs ys
             where longer a b n = maximumBy (compare `on` length)
                                        (map (filter (==n)) [a, b])

-- | Given an Integer return the list of its prime factors.
primeFactors :: Integer -> [Integer]
primeFactors n = primeFactorsIter n $ takeWhile (lt_sqrt n) primes
    where primeFactorsIter n ps
            | n <= 1         = []
            | length ps == 0 = [n]
            | otherwise      = let p = head ps  -- we check for empty <ps> above
                                   q = quot n p in
                                 case divides n p of
                                     True  -> p : primeFactorsIter q ps
                                     False -> primeFactorsIter n $ tail ps

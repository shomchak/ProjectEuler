module Main where

import System.Environment (getArgs)
import Data.List (foldl')

import Primes (primes)

main :: IO ()
main = do args <- getArgs
          putStrLn $ show $ solve' $ read $ args !! 0

-- | Accumulate a list of primes and reduce them at the end.
solve :: Integer -> Integer
solve n = foldl' (*) 1 $ takeWhile (<=n) primes >>= primeContent n
            where primeContent n p | p > n     = []
                                   | otherwise = p : (primeContent (quot n p) p)

-- | Accumulate a product of primes as you calculate them.
solve' :: Integer -> Integer
solve' n = foldl' (\ acc p -> acc * p ^ (primeContent n p)) 1 $ takeWhile (<=n) primes
            where primeContent n p | p > n     = 0
                                   | otherwise = 1 + (primeContent (quot n p) p)


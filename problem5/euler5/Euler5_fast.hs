module Main where

import System.Environment (getArgs)
import Data.List (foldl')

import Primes (primes)

main :: IO ()
main = do args <- getArgs
          putStrLn $ show $ solve $ read $ args !! 0

solve :: Integer -> Integer
solve n = foldl' (*) 1 $ takeWhile (<=n) primes >>= primeContent n
            where primeContent n p | p > n     = []
                                   | otherwise = p : (primeContent (quot n p) p)

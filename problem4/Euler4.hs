module Euler4 where

import Data.List (sortBy)

-- | Descend the products and return the first palindrome.
solve :: (Integral a, Show a) => a
solve = head $ filter isPalindrome $ sortBy (flip compare) products

products :: (Integral a) => [a]
products = [x * y | x <- [999,998..100], y <- [x,x-1..100]]

isPalindrome :: (Show a) => a -> Bool
isPalindrome n = str == reverse str where str = show n


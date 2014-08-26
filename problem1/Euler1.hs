module Euler1 where

solve :: Int
solve = sum [ n | n <- [1..limit], mod n 3 == 0 || mod n 5 == 0]
    where limit = 999

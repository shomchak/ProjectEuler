module Euler6 where

solve = (sum $ map (^2) ns) - ((sum ns) ^ 2) where ns = [1..100]

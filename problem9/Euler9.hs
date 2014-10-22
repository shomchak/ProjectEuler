module Euler9 where

solve :: [(Integer, Integer, Integer)]
solve = filter (\(a, b, c) -> a * a + b * b == c * c) $ sum_triples 1000
  where sum_triples total =
          do a <- [1..quot total 3]
             b <- takeWhile (\b -> total - a - b > b) [a+1..total]
             return (a, b, total - b - a)

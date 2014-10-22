module Euler8 where
import Data.List (foldl')
import Data.Functor ((<$>))

solve = foldl' max 0 <$> products <$> ns
  where ns = map (read . (:[])) . head . lines
          <$> readFile "e8input.txt" :: IO [Int]
        products ns
          | length ns < 5 = []
          | otherwise     = product (take 5 ns) : products (tail ns)

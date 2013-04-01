module Main where
import System.Environment

solve_it :: (Integral a) => a -> a
solve_it limit = sum [ n | n <- [1..limit], mod n 3 == 0 || mod n 5 == 0]

main :: IO ()
main = do
    putStrLn(show (solve_it 999))

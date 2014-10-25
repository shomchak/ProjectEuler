module PrimeSieve (primes) where
import Data.List (foldl')
import System.Environment (getArgs)
import qualified Data.Map.Strict as M

main :: IO ()
main = getArgs >>= print . show . head . primes . read . (flip (!!)) 0

type CompositeMap a = (M.Map a [a])
data GenState a = GenState (CompositeMap a) [a]

-- | Return all primes below a limit.
primes :: Integral a => a -> [a]
primes n = ps
  where (GenState _ ps) = foldl' step (GenState M.empty []) [2..n]

step :: Integral a => GenState a -> a -> GenState a
step (GenState comp_map primes) guess
  | M.member guess comp_map = GenState (updateComposite comp_map guess) primes
  | otherwise               = GenState (M.insert (guess*guess) [guess] comp_map)
                                       (guess:primes)

updateComposite :: Integral a => CompositeMap a -> a -> CompositeMap a
updateComposite cmap guess =
  foldl' (\cmap' (c, ps) -> M.insert c ps cmap') cmap cps
    where cps = do p <- M.findWithDefault [] guess cmap
                   let c = guess + p
                   let ps = M.findWithDefault [] c cmap
                   return (c, p:ps)

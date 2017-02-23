import Euler

perms 0 x = x
perms 1 x = x
perms n x = (x !! facInd) : perms (n - maxFac) (removeAt facInd x) where
    maxFac | fac (length x - 1) >= n = 0
           | otherwise = facInd * fac (length x - 1)
    facInd = n `div` (fac (length x - 1) + 1)
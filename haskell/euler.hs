module Euler where

import Data.Char

sumOfDigits :: (Integral a) => Integer -> Integer
sumOfDigits 0 = 0
sumOfDigits x = (mod x 10) + (sumOfDigits (div x 10))

sumOfDigits' :: (Integral a) => Int -> Int
sumOfDigits' x = sum $ map digitToInt $ show x

sumOfSqDigits :: (Integral a) => Integer -> Integer
sumOfSqDigits 0 = 0
sumOfSqDigits x = (mod x 10)^2 + (sumOfSqDigits (div x 10))

sumOfFacDigits :: (Integral a) => Integer -> Integer
sumOfFacDigits 0 = 0
sumOfFacDigits x = fac' (mod x 10) + sumOfFacDigits (div x 10)

fac' :: Integral a => a -> a
fac' 0 = 1
fac' x = product [1..x]

fac :: Integral a => a -> a
fac 0 = 1
fac x = x * fac (x - 1)

removeAt :: Int -> [a] -> [a]
removeAt n x = x1 ++ tail x2 where (x1, x2) = splitAt n x

fib :: Int -> Integer
fib n = fibHelper n 1 1 0

-- function to calculate fibonacci, n is target index, curr is current index, fib1 and fib2 is fibonacci value of index curr-1 and curr-2 respectively
fibHelper :: Int -> Int -> Integer -> Integer -> Integer
fibHelper n curr fib1 fib2 | curr == n = fib1
					 	   | otherwise = fibHelper n (curr+1) (fib1+fib2) fib1

fibL x = fibLength 1 1 0 x

-- function to calculate index of first fibonacci value bigger then x
fibLength n fib1 fib2 x | fib1 > x = n
						| otherwise = fibLength (n+1) (fib1+fib2) fib1 x

divisors :: Integral a => a -> [a]
divisors n = 1 : (divsTillSqrt ++ map (div n) divsTillSqrt) where divsTillSqrt = filter (divBy n) [2..(floor $ sqrt $ fromIntegral n)]

divBy n m = n `mod` m == 0

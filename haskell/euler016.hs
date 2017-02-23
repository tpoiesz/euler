sumOfDigits :: (Integral a) => Integer -> Integer
sumOfDigits 0 = 0
sumOfDigits x = (mod x 10) + (sumOfDigits (div x 10))

main = print (sumOfDigits (product(replicate 1000 2)))
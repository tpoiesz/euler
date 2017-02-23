numDiv x = (length $ divisors x) * 2

divisors :: Integral a => a -> [a]
divisors x = [y | y <- [1..root x], mod x y == 0] where root x = floor $ sqrt $ fromIntegral x

sumTill :: Integral a => a -> a
sumTill 0 = 0
sumTill x = sum[1..x]

triangulars = map (sumTill) [1..]
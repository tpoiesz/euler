fifthpowerdigitsum 0 = 0
fifthpowerdigitsum n = fifthpowerdigitsum (n `div` 10) + lastdigit^5 where lastdigit = n `mod` 10
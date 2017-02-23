import Euler

squareDigitChain 1 = 1
squareDigitChain 89 = 89
squareDigitChain x = squareDigitChain $ sumOfSqDigits x

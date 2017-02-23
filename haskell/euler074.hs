import Euler

facDigitChain 1 = 1
facDigitChain 145 = 1
facDigitChain 169 = 3
facDigitChain 871 = 2
facDigitChain 872 = 2
facDigitChain x = facDigitChain (sumOfFacDigits x) + 1

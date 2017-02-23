import euler as e


def isLychrel(num):
    for i in range(0, 50):
        num += int(str(num)[::-1])
        if e.isPalindrome(str(num)):
            return True
    return False


print len([num for num in range(1, 10000) if not isLychrel(num)])

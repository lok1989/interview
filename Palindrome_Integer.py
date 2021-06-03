# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import math


def check_palindrome(param):
    x = param
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        rev = 0
        while x > 10:
            num = x % 10
            rev = (num + rev)
            x = int(x / 10)
            rev *= 10
            if x < 10:
                rev = rev + x

        if rev == param:
            return True
        else:
            return False


if __name__ == '__main__':
    i = 123234455321
    print(check_palindrome(i))

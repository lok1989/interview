# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
if __name__ == '__main__':
    d = 4
    f = 6
    target = 3

    dices = []

    if d != 1 and target < d:
        print("Not achievable")
        sys.exit(0)

    i = 0
    while i < d:
        dices.append(list(range(1,f)))
        i += 1


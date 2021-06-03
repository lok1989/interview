"""
Check if parenthesis are matched correctly.
"""


def isValid(s):
    stack = []
    map = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in map:
            top_element = stack.pop()
            if map[top_element] != top_element:
                return False
        else:
            stack.append(char)


if __name__ == '__main__':
    print(isValid('{}{}{}[]'))

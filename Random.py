# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    found = []
    not_found = []
    result =[]

    for i in arr1:
        if i in arr2:
            found.append(i)
        else:
            not_found.append(i)

    # found = [2,3,1,3,2,4,6,9,2]

    for i in range(len(arr2)):
        for j in range(len(found)):
            if arr2[i] == found[j]:
                result.append(found[j])

    result = result + not_found
    print(result)
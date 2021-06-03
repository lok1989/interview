"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the
product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""
import math

# This method uses division
def dcp2(input):

    if 0 in input:
        return None
    all_product = 1
    output = []
    for lok in input:
        all_product *= lok
    for lok in range(0, len(input)):
        output.append(math.trunc(all_product / input[lok]))
    return output


# This method does not use division
def dcpv2(input):
    if 0 in input:
        return None
    output = []
    for i in range(0, len(input)):
        product = 1
        for j in range(0, len(input)):
            if i is j:
                continue
            else:
                product *= input[j]
        output.append(product)

    return output


if __name__ == '__main__':
    i = [1, 2, 3, 4, 5]
    j = [3,2,1,4,0]
    print("Finding answer using division " + str(dcp2(i)))
    print("Finding answer without division " + str(dcpv2(i)))
    print("Finding answer using division " + str(dcp2(j)))
    print("Finding answer without division " + str(dcpv2(j)))

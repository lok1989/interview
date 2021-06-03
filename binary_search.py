import time


def binary_search(ip_list, ip_target):
    first = 0
    last = len(ip_list) - 1

    '''
     Target = 4
     I = [0,1,2,3,4,5,6,7,8,9]   
     V = [0,1,2,3,4,5,6,7,8,9]   
        
    '''

    while first <= last:
        current_index = (first + last) // 2
        if ip_list[current_index] == ip_target:
            return current_index
        elif ip_list[current_index] > target:
            last = current_index
        else:
            first = current_index
    return -1


if __name__ == '__main__':
    input_list = list(range(3, 1000))
    target = 345
    result = binary_search(input_list, target)
    if result < 0:
        print("Target not found in the list")
    else:
        print("Target found in the position :", result)

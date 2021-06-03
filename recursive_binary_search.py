def recursive_binary_search(ip_list, ip_target):


    '''
     Target = 4
     I = [0,1,2,3,4,5,6,7,8,9]   
     V = [0,1,2,3,4,5,6,7,8,9]
    '''
    if len(ip_list) is 0:
        return False
    else:
        midpoint = len(ip_list) // 2

    if ip_list[midpoint] == ip_target:
        return True
    else:
        if ip_list[midpoint] < target:
            return recursive_binary_search(ip_list[midpoint + 1:], ip_target)
        else:
            return recursive_binary_search(ip_list[: midpoint], ip_target)


if __name__ == '__main__':
    input_list = list(range(0, 5))
    target = 40
    result = recursive_binary_search(input_list, target)
    print("Item found in the List:", result)

def linear_search(ip_list, ip_target):
    for i in range(0, len(ip_list)):
        if ip_list[i] == ip_target:
            return i
    return -1


if __name__ == '__main__':
    input_list = list(range(1, 100))
    target = 8
    result = linear_search(input_list, target)
    if result < 0:
        print("Target not found in the list")
    else:
        print("Target found in the position :", result)

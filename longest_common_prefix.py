def longest_common_prefix(strs):
    if len(strs) == 0:
        return 0
    lcp = 0
    for i in range(len(min(strs, key=len))):
        c = strs[0][i]
        if all(a[i] == c for a in strs):
            lcp += 1
        else:
            break

    return strs[0][:lcp]


if __name__ == '__main__':
    strs = ["cir", "car"]
    op = longest_common_prefix(strs)
    print(op)

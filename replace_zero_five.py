def rzerofive(ip_num):
    ip = ip_num
    answer = 0
    exponent = 0
    while ip > 0:
        n = ip % 10
        if n == 0:
            answer = answer + (5 * pow(10, exponent))
        else:
            answer = answer + (n * pow(10, exponent))
        exponent += 1
        ip = ip // 10
    print(answer)


if __name__ == '__main__':
    i = 10500
    rzerofive(i)

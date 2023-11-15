def fibonacci(num):
    a, b = 1, 1     # 设定前2项的值
    num_binary = bin(num).replace("0b1", "")    # 转换为二进制，便于后续计算
    for bit in num_binary:
        is_odd = True if bit == "1" else False  # 判断当前是奇数幂还是偶数幂
        aa, bb, ab = a * a, b * b, a * b    # 计算中间值
        if is_odd:
            a, b = aa + ab + ab, aa + bb
        else:
            a, b = aa + bb, ab + ab - bb
    return a


if __name__ == "__main__":
    n = 1024
    print(f"爬到1024级台阶的方法数={fibonacci(n)}")



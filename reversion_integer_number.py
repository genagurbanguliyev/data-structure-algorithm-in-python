def reverse_integer(num: int) -> int:
    flag = False
    if num < 0:
        flag = True
        num = abs(num)
    reversed = 0
    remainder = 0

    while num > 0:
        remainder = num % 10
        num = num // 10
        reversed = reversed * 10 + remainder
    return reversed*(-1) if flag else reversed

if __name__ == '__main__':
    print(reverse_integer(123))
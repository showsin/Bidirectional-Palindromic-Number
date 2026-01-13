import threading

from sympy.physics.units import current


# 判断当前数是否是回文数
def is_palindrome(str_num):
    # 负数不是回文数
    if int(str_num) < 0:
        return False
    return str_num == str_num[::-1]

# 查找小于当前数的最近回文数
def find_nearest_palindrome_0(str_num):
    # count_0 记录负向查找次数
    count_0 = 0
    # i_0 记录小于当前数的最近回文数
    for i_0 in range(int(str_num) - 1, 0, -1):
        # 循环判断当前数是否是回文数并增加负向查找次数
        count_0 += 1
        if is_palindrome(str(i_0)):
            return i_0,count_0


# 查找大于当前数的最近回文数
def find_nearest_palindrome_n(str_num):
    # count_n 记录正向查找次数
    count_n = 0
    # i_n 记录大于当前数的最近回文数 左闭右开的10**len(str_num)能取到对应位数的数字的最大回文数（例如10**3能取到3位数的数字的最大回文数999）
    for i_n in range(int(str_num) + 1, 10**len(str_num)):
        # 循环判断当前数是否是回文数并增加正向查找次数
        count_n += 1
        if is_palindrome(str(i_n)):
            return i_n,count_n

# 以max_step为一轮，双向查找最近回文数
def find_nearest_palindrome_100(start_num,direction,max_step=100):
    current = start_num
    distance = 0
    for i in range(max_step):
        current += direction
        distance += 1
        if is_palindrome(str(current)):
            return current,distance


def main():
    # 循环判断输入是否是整数
    while True:
        try:
            int_num = int(input('请输入一个整数:'))
            break
        except ValueError:
            print('输入有误!')
    str_num = str(int_num)
    # 先判断输入的数是否是回文数并
    if is_palindrome(str_num):
        print(f'{str_num} 本身就是回文数')
        return

    # # 查找小于当前数的最近回文数并返回回文数和负向查找次数
    # i_0,count_0 = find_nearest_palindrome_0(str_num)
    # # 查找大于当前数的最近回文数并返回回文数和正向查找次数
    # i_n,count_n = find_nearest_palindrome_n(str_num)
    # # 比较负向查找次数和正向查找次数, 输出最近的回文数
    # if count_0 == count_n:
    #     print(f'{str_num} 最近的回文数是 {i_0}和{i_n}')
    # elif count_0 < count_n:
    #     print(f'{str_num} 最近的回文数是 {i_0}')
    # else:
    #     print(f'{str_num} 最近的回文数是 {i_n}')

    # 以100为一轮，双向查找最近回文数，直至找到最近回文数
    total_distance_0 = 0
    total_distance_n = 0
    while True:
        # 递归查找小于当前数的最近回文数和大于当前数的最近回文数
        i_100_0,distance_0 = find_nearest_palindrome_100(int_num,-1,100)
        i_100_n,distance_n = find_nearest_palindrome_100(int_num,1,100)
        total_distance_0 += distance_0
        total_distance_n += distance_n
        i_100_0, distance_0 = find_nearest_palindrome_100(i_100_0, -1, 100)
        i_100_n, distance_n = find_nearest_palindrome_100(i_100_n, 1, 100)
        total_distance_n += distance_n
        total_distance_0 += distance_0
        if is_palindrome(str(i_100_0)) or is_palindrome(str(i_100_n)):
            break
        # print(f'{str_num} 最近的回文数是 {i_100_0}和{i_100_n}，分别距离当前数{distance_0}和{distance_n}')


if __name__ == '__main__':
    main()

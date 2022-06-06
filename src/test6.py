"""
 * Project name(项目名称)：Python考试题
 * Package(包名): 
 * File(文件名): test6
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/6/6 
 * Time(创建时间)： 14:44
 * Version(版本): 1.0
 * Description(描述)： 4.8
 """

from itertools import permutations


def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    digits = (1, 2, 3, 4)
    for i in range(1, len(digits) + 1):
        for number in permutations(digits, i):
            number = int(''.join(map(str, number)))
            if isPrime(number):
                print(number)

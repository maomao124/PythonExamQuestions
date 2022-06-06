"""
 * Project name(项目名称)：Python考试题
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/6/6 
 * Time(创建时间)： 14:29
 * Version(版本): 1.0
 * Description(描述)： 4.5
 """
import random

if __name__ == '__main__':
    x = [random.randint(0, 100) for i in range(20)]
    print(x)

    x[::2] = sorted(x[::2], reverse=True)

    print(x)

"""
 * Project name(项目名称)：Python考试题
 * Package(包名): 
 * File(文件名): test4
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/6/6 
 * Time(创建时间)： 14:32
 * Version(版本): 1.0
 * Description(描述)： 4.6
 """

if __name__ == '__main__':
    x = input("请输入小于1000的整数：")
    x = eval(x)
    t = x
    i = 2
    result = []
    while True:
        if t == 1:
            break
        if t % i == 0:
            result.append(i)
            t = t // i
        else:
            i += 1

    print(x, "=", "*".join(map(str, result)))

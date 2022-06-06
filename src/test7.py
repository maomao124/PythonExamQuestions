"""
 * Project name(项目名称)：Python考试题
 * Package(包名): 
 * File(文件名): test7
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/6/6 
 * Time(创建时间)： 14:57
 * Version(版本): 1.0
 * Description(描述)： 4.9
 """


def getY(x):
    """
    根据x的值计算y的值
    :param x: x
    :return: y
    """
    if 0 < x < 5:
        return x
    elif 5 < x < 10:
        return 3 * x - 5
    elif 10 < x < 20:
        return 0.5 * x - 2
    else:
        return 0


if __name__ == '__main__':
    x = input("请输入x的值：")
    x = eval(x)
    print("y的值为：", getY(x))

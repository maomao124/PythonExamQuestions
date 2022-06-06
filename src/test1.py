"""
 * Project name(项目名称)：Python考试题
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/6/6 
 * Time(创建时间)： 14:12
 * Version(版本): 1.0
 * Description(描述)： 4.2
 """

if __name__ == '__main__':
    inputYear = input("请输入年份:")
    inputYear = eval(inputYear)
    if inputYear < 0:
        print("输入错误")
        exit(0)
    if inputYear % 400 == 0 or (inputYear % 4 == 0 and not inputYear % 100 == 0):
        print("是闰年")

    else:
        print("不是闰年")

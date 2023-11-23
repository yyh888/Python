# if 表达式1:
#     语句块
# elif 表达式2:
#     语句块
# else:
#     语句块


# choice = input("选择A或者B: ")
# if choice=="A":
#     print("答对了")
# elif choice=="B":
#     print("答错了")
# else:
#     print("输1入错误")


# a = input("请输入一个数字: ")
# b = input("请输入一个数字: ")
# if a == "1":
#     if b == "2":
#         print("aaaaaa")
#     print("bbbbbb")
# print("cccccc")


# a = input("请输入一个数字: ")
# if(a == "1"):
#     # 什么都不做
#     pass
# else:
#     print("bbbbb")


# a = 1
# while a <= 5:
#     print(a)
#     a += 1


num = 1
# 结果是sum
sum = 0
while num <= 5:
    tmp = 1
    i = 1
    while i <= num:
        tmp *= i
        i += 1
    sum += tmp
    num += 1

print(sum)
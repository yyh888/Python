# a = [1, 2, 3, 4]
# a.append(5)
# print(a)

# class MyClass:
#     def __init__(self):
#         self.l = 1
#         self.r = 2
#
#     def fun(self):
#         p = 100
#
# x = MyClass()
# print(x.r)


# def Fib(n):
#     if n < 2:
#         return n
#     return Fib(n - 1) + Fib(n - 2)
#
# n = int(input())
# for i in range(1, n + 1):
#     print(Fib(i), end = ' ')


# a = [1, 2, 3, 4, 5]
# b = [7, 8, 9]

# for i in range(len(b)):
#     a[i] = b[i]

# a = b[:2]
#
# print(a)

# for i in range(1, 10):
#     for j in range(1, 10):
#         print("%d*%d = %d"%(i, j, i * j), end = ' ')
#         if i == j:
#             break
#     print("\n")


# import time
#
# for i in range(4):
#     print(i)
#     time.sleep(1)

import math

# def isPrime(n):
#     for i in range(2, round(math.sqrt(n) + 1)):
#         if n % i == 0:
#             return False
#     return True
#
# for i in range(100, 201):
#     if isPrime(i):
#         print(i, end = ' ')


# def fun(num):
#     s = str(num)
#     One = int(s[-1])
#     ten = int(s[-2])
#     hun = int(s[-3])
#     Res = One ** 3 + ten ** 3 + hun ** 3
#     if Res == num:
#         return True
#     return False
#
# for i in range(100, 1000):
#     if(fun(i)):
#         print(i, end = ' ')

# flag = False
# target = int(input("请输入一个数字: "))
# print(f"{target} = ", end = '')
# if(target < 0):
#     print(-1, "*", end = '')
#
# while True:
#     if flag:
#         break
#     for i in range(2, int(target + 1)):
#         if target % i == 0:
#             print("%d"%i, end = '')
#             if i == target:
#                 flag = True
#                 break
#             print("*", end = '')
#             target /= i
#             break


# n = int(input("请输入一个整数: "))
# s = str(n)
# print("有%d位数"%len(s))
# print(s[::])


# weekT = { 'h': 'thursday',
#           'u': 'tuesday'}
#
# weekS={'a':'saturday',
#        'u':'sunday'}
# week={'t': weekT,
#       's': weekS,
#       'm':'monday',
#       'w':'wensday',
#       'f':'friday'}
#
# S1 = week[input("输入第一个字母: ").lower()]
# if S1 == weekT or S1 == weekS:
#     S2 = S1[input("请输入第二个字母: ").lower()]
#     print(S2)
# else:
#     print(S1)

# class MyClass:
#     i = 100
#
#     def __init__(self, num):
#         i = num
#
# x = MyClass(200)
# print(x.i)


# L = [1,2,3,4,5]
# # print(''.join(str(n) for n in L))
# s = ""
# for i in range(len(L)):
#     s += str(L[i])
#
# print(s)


# def hello():
#     print('Hello World!')
# def helloAgain():
#     for i in range(2):
#         hello()
#
# if __name__=='__main__':
#     helloAgain()


# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(a[1][2])


def QuickSOrt(nums, left, right):
    if left >= right:
        return
    key = nums[left]
    l, r = left, right
    while l < r:
        while l < r and nums[r] >= key:
            r -= 1
        while l < r and nums[l] <= key:
            l += 1
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]
    nums[l], nums[left] = nums[left], nums[l]
    QuickSOrt(nums, left, l - 1)
    QuickSOrt(nums, l + 1, right)

a = [1, 5, 3, 6, 4]
QuickSOrt(a, 0, len(a) - 1)
print(a)

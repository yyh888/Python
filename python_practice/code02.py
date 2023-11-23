# a = {(1, 2, 3), "aaa"}
#

# total = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != j and j != k and i != k:
#                 total += 1
#
# print(total)

# profit = int(input('show me the money: '))
# bonus = 0
# a = (100000, 100000, 200000, 200000, 400000)
# rates = (0.1, 0.075, 0.05, 0.03, 0.015, 0.01)
# for i in range(len(a)):
#     if profit <= a[i]:
#         bonus += profit * rates[i]
#         profit = 0
#         break
#     else:
#         bonus += a[i] * rates[i]
#         profit -= a[i]
# bonus += rates[-1] * profit
# print(bonus)
#


# def isLeapYear(y):
#     return (y % 400 or (y % 4 == 0 and y % 100 != 0))
#
# Day = [0,31,28,31,30,31,30,31,31,30,31,30]
# res = 0
# year=int(input('Year:'))
# month=int(input('Month:'))
# day=int(input('day:'))
# if(isLeapYear(year)):
#     Day[2] += 1
#
# for i in range(month):
#     res += Day[i]
#
# print(res + day)

raw = []
for i in range(3):
    x = int(input('int%d: ' % (i)))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i + 1, len(raw)):
        if raw[i] > raw[j]:
            raw[i], raw[j] = raw[j], raw[i]

print(raw)
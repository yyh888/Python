# class Functor:
#     def __init__(self, val):
#         self.m_Val = val
    
#     def __call__(self):
#         func(self.m_Val)

# def func(num):
#     print(2 * num)

# num = 100
# x = Functor(num)
# x()

lstS = [1, 2, 3, 4, 5]
# e = enumerate(lstS, start = 1)
# for iIdx, iVal in e:
#     print(iIdx, iVal)

for i in enumerate(lstS):
    print(i[1])
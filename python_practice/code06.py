import copy
iList1 = [[1, 2], 3, 4, 5]
# List2 = iList1

# iList1[0] = 'abc'
# print(iList1)

# iList2 = copy.copy(iList1)
# iList1[0] = 'abcdef'
# print(iList2)

iList2 = copy.deepcopy(iList1)
iList1[0][1] = 'aaaaa'
print(iList2)


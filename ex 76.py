list1 = [x for x in range(8)]
list2 = [x for x in range(0,8,2)]

list3 = [x+y for x,y in zip(list1, list2)]

print(list3)

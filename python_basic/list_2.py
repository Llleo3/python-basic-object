#tuple 元组
a_tuple=(1,2,3,4,5,6)
another_tuple=2,3,12,43

a_list=[1,23,12,4,123,5,23,2,3,23,23,32,23]
print(a_tuple+another_tuple)
print(a_tuple+another_tuple+tuple(a_list))
for centent in a_list:
    print(centent)
for index in range(len(a_tuple)):
    print('index=',index,'num in a_tuple=',a_tuple[index])
print(a_list[2])
print(a_list[1:])         #第一位到最后
print(a_list[-1])
print(a_list.index(23))   #23首次出现的顺序
print(a_list.count(23))   #23出现的次数
a_list.sort()    #从小到大排序
print(a_list)
a_list.sort(reverse=True)
print(a_list)    #从大到小排序
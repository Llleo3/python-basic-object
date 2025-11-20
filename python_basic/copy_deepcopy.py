import copy
a=[1,2,3]
b=a
print(id(a))    #id 表示对象在内存中的地址（唯一）
print(id(b))
b[0]=10
print(a)
a[2]=6
print(b)
print(id(a)==id(b))

c=copy.copy(a)    #copy 内容一致 地址不同，改变a不能改变c 若a=[1,2,[3,4]],改变a[2][1],c会发生变化
print(c)
print(id(a)==id(c))
print(a==c)
a=[1,2,3,[1,2,4]]
d=copy.copy(a)
a[3][0]=5
print(a[3][0]==d[3][0])

e=copy.deepcopy(a)
print(id(a[3])==id(e[3]))
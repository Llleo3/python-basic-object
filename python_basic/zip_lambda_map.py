a=[1,2,3]
b=[4,5,6]
zip(a,b)
print(zip)
print(list(zip(a,b)))
for i,j in list(zip(a,b)):
    print(i/2,j*2)
print(list(zip(a,a,b)))

def fun1(x,y):
    return(x+y)
print(fun1(2,1))
#lambda 表示定义匿名函数
print((lambda x,y:x+y) (1,4))
print(map(fun1,[1],[2]))
print(list(map(fun1,[1,3,1,9],[2,4,53,1])))  #列表中的元素通过fun1一一对应相加
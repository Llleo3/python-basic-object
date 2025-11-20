a_list=[1,4,2,5,6]
tuple=(23,123,321,412,3)
dictionary={'apple':1,'pear':{2:'r'},'orange':3}
d1={1:'a','b':'c'}
print(dictionary['pear'][2])
print(dictionary['apple'],a_list[2],tuple[2])
#delete del  删除
del dictionary['apple']
print(dictionary)
dictionary['b']=20  #添加‘b’:20
print(dictionary)
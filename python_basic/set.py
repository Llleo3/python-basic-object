#set 找不重复的元素 用于集合{}
char_list=[1,2,3,1,1,1,3,4]
print(type(set(char_list)))
print(type({'w':1}))
sentence='This is the python'
print(set(sentence))
u_char=set(char_list)
u_char.add('肌肉')
u_char.add('f')
#u_char.clear()  #清除
u_char.remove('f')
print(set(u_char))
print(u_char.remove('肌肉'))
print(u_char.discard("y"))
print(set(u_char))

set1=u_char
set2={1,'a','v'}
print(set1.difference(set2))
print(set2.difference(set1))


'''a=True
while a:
    b=int(input('type something:'))
    if b==1:
        a=False
    else:
        pass
print('finish run')'''

#break:if b=1，会跳出while_loop，打印 finish run。  continue:if b=1，会继续执行while_loop。
'''while True:
    b=int(input('type something:'))
    if b==1:
        break
    else:
        pass
    print('still in while')
print('finish run')'''

while True:
    b=int(input('type something:'))
    if b==1:
        continue
    else:
        pass
    print('still in while')
print('finish run')
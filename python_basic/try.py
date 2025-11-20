#try 错误处理
try:
    file=open('eeee','r+')
except Exception as e:
    print('There is no file named as eeee')
    reply=input('Do you want to create a new file ?'+' Y/N')
    if reply=='Y':
        file=open('eeee','w')
    else:
        pass
else:
    file.write('ssss')
    file.close()
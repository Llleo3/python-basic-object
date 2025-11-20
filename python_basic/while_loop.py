
print("求平均值")
total=0
count=0
#result=total/count
user_input=input("请输入数字(输入q退出程序):")
while user_input!= "q":
    num=float(user_input)
    total=total+num
    count=count+1
    user_input=input("请输入数字(输入q退出程序):")
if count==0:
    result=0
else:
    result=total/count
print("所求平均值为："+str(result))


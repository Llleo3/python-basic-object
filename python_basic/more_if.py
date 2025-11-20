user_gender=input("请输入你的性别:")
#询问性别并回复
if user_gender=="男":
    print("hello,sir")
elif user_gender == "女":
    print("泥嚎")
else:
    print("不像人类")
#询问身体状态并回复
#身体状态指数(BSI)>80
#60<身体状态指数（BSI)<80
#身体状态指数（BSI）<60
boby_status_index=int(input("今天身体状态:"))
if boby_status_index>80:
    print("今天去健身房")
elif 60<boby_status_index<80:
    print("不去健身房，去跑步")
else:
    print("休息日，躺着休息")






#BMI=体重/（身高**2）
user_weight=float(input("请输入你的体重（单位：kg）："))
user_height=float(input("请输入你的身高（单位：m）："))
user_BMI=user_weight/(user_height)**2
print("你的BMI值:"+str(user_BMI))

#偏瘦:user_BMI<=18.5
#正常:18.5<user_BMI<=25
#偏胖:25<user_BMI<=30
#肥胖:user_BMI>30
if user_BMI <=18.5:
    print("属于偏瘦")
elif 18.5<user_BMI<=25:
    print("属于正常")
elif 25<user_BMI<=30:
    print("属于偏胖")
elif user_BMI>30:
    print("属于肥胖")

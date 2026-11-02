a = int(input("请输入身高（米）"))
b = int(input("请输入体重（千克）"))
bmi = b/(a*a)
if bmi < 18.5:
    print("BMI指数为：",bmi,"体重过轻")
if bmi >= 18.5 and bmi < 24:
    print("BMI指数为：",bmi,"体重正常")
if bmi >= 24 and bmi < 28:
    print("BMI指数为：",bmi,"体重过重")
if bmi >= 28:
    print("BMI指数为：",bmi,"肥胖")
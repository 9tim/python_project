#性別
gender = input("請輸入你的性別(男/女) :")
#年齡
age = int(input("請輸入你的年齡 :"))
#身高
height = float(input("請輸入你的身高(CM) :"))
#體重
weight = float(input("請輸入你的體重(公斤) :"))
#體脂率
Body_fat_percentage = float(input("請輸入你的體指率(百分比) :"))
#活動因子
activity_factor = float(input("每週運動天數 \n   0天 : 1.2 \n 1~3天 : 1.375 \n 3~5天 : 1.55 \n 6~7天 : 1.725 \n 6~7天 : 1.725 \n 幾乎整天 : 1.9  \n 請輸入你的活動因子 : "))
#壓力因子
stress_factor = float(input("壓力狀況 \n 正常 : 1.0 \n 發燒 : 1.13 \n 小手術、癌症 : 1.2 \n 骨骼受傷 : 1.3 \n 癌症惡質病 : 1.2~1.4 \n 懷孕 : 1.1 \n 哺乳 : 1.4 \n 生長期 : 1.4 \n 敗血症 : 1.4~1.8 \n 燒傷 : 1.7~2.2 \n 請輸入你的活動因子 : "))

#各項計算
#BMI
BMI = weight/(height/100)**2

if BMI < 18.5:
    BMI_status = "體重過輕"
elif BMI >= 18.5 and BMI < 24:
    BMI_status = "正常"
elif BMI >= 24 and BMI < 27:
    BMI_status = "過重"
elif BMI >= 27 and BMI < 30:
    BMI_status = "輕度肥胖"
elif BMI >= 30 and BMI < 35:
    BMI_status = "中度肥胖"
else: BMI_status = "重度肥胖"

#除體之重
In_addition_to_body_weight = weight*((100-Body_fat_percentage)/100)

#基礎代謝率
if  gender == "男":
    BMR = 66+(13.7*weight+5*height-6.8*age)
else :  
    BMR = 66+(9.6*weight+1.8*height-4.7*age)

#總熱量消耗
TDEE = BMR*activity_factor*stress_factor

#碳水化合物
carbohydrate = (TDEE*0.2)/4

#蛋白質
protein = (TDEE*0.3)/4
#脂肪
Fat = (TDEE*0.5)/9
#結果
print("----------您的健康飲食推薦報告--------------")
print("您的BMI為 : ", BMI)
print("您的除體脂重:",In_addition_to_body_weight)
print("您的體重狀態為:",BMI_status)
print("您的體脂率為:",Body_fat_percentage,"%")
print("您的基礎代謝率為:",BMR)
print("您的總熱量消耗為:",TDEE)
print("----------您的三大營養素建議克數為--------------")
print("碳水化合物 : ", carbohydrate,"克")
print("蛋白質 : ", protein,"克")
print("脂肪 : " ,Fat,"克")





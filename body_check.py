import sys
import time

#This is a uncompleted file for a simple body check
#I uploaded this for testing my Github account
#You can use this for business(even I think no one will use this 'wonderful' code)

#启动
def begin():
    global name
    print("欢迎来到第五医院体检程序 @sky_ming 2024/1/19")
    time.sleep(0.8)
    name=input("请输入你的昵称：")
    time.sleep(0.8)
    print("亲爱的"+name+"，欢迎你来到体检中心！")
    time.sleep(0.8)
    print("下面开始体检！")
    time.sleep(0.8)
    print(" ")
    time.sleep(0.8)
    

#基本信息
def basic():
    global height,weight,bmi,height_cm,situation
    time.sleep(0.8)
    print("下面开始基本检查！")
    time.sleep(0.8)
    height_cm=int(input("请输入你的身高(cm)："))
    height=float(height_cm*0.01)
    time.sleep(0.8)
    weight=float(input("请输入你的体重(kg)："))
    bmi=round(weight/(height*height),2)
    time.sleep(0.8)
    print("你的BMI体重指数是："+str(bmi))
    bmi_bool=1
    time.sleep(0.8)
    if bmi<=18.5 and bmi>1:
        situation="超轻"
    elif bmi>18.5 and bmi<=24:
        situation="正常"
    elif bmi>24 and bmi<=28:
        situation="超重"
    elif bmi>28 and bmi<=32:
        situation="肥胖"
    elif bmi>32:
        situation="重度肥胖"
    else:
        bmi_bool=0
        situation="计算结果出错"
    time.sleep(0.8)
    if bmi_bool==1:
        print("按照亚洲人体重指数标准,你的体重状况是："+situation)
    else:
        print("结果出错啦！程序即将结束，请重新运行程序！ @sky_ming 2024/1/19")
        sys.exit

#基础结果输出
def out_ba():
    time.sleep(0.8)
    print("您的身高体重分别为："+str(height_cm)+"cm/"+str(weight)+"kg")
    time.sleep(0.8)
    print("您的BMI体重指数为："+str(bmi))
    time.sleep(0.8)
    print("按照亚洲人体重指数标准，您的体重状况为："+situation)



#进阶检查分科室
def out():
    print("我是外科检查程序，我还没写好哦！")

def inside():
    print("我是内科检查程序，我还没写好哦！")

def china():
    print("我是中医科检查程序，我还没写好哦！")

#进阶检查总执行
def improved_check():
    global im_b
    print("下面开始进阶检查！")
    time.sleep(0.8)
    check_kind=int(input("请输入你要做的检查项目(外科1，内科2，中医3，跳过0):"))
    time.sleep(0.8)
    if check_kind==0:
        print("进阶检查已跳过！")
        im_b=0
    elif check_kind==1:
        out()
    elif check_kind==2:
        inside()
    elif check_kind==3:
        china()
    else:
        print("菜就多练！ @sky_ming 2024/1/19")
        time.sleep(0.8)
        sys.exit

#进阶检查结果
def out_im():
    print("进阶检查尚未制作，敬请期待！")
    time.sleep(0.8)
    0


#输出体检报告
def output():
    print("体检圆满结束！以下是你的体检报告")
    time.sleep(0.8)
    print("受检者昵称："+name)
    time.sleep(0.8)
    out_ba()
    if im_b==0:
        print("进阶检查已跳过！")
    else:
        out_im()
    time.sleep(0.8)



def main():
    begin()
    time.sleep(0.8)
    basic()
    time.sleep(0.8)
    improved_check()
    time.sleep(0.8)
    output()
    time.sleep(0.8)




main()
print("程序已顺利完成运行，感谢您的使用！再会！ @sky_ming 2024/1/19")
time.sleep(0.8)
sys.exit
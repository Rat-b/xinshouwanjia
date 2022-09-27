from msilib.schema import File
import random
from tkinter import W


operator = ['+','-']
vis = []#储存已经生成的题目列表以防重复
answer = []
value=input("请输入一个整数： ")
while True:
    if (value.isdigit()):
        n = int(value)
        break
    else:
        print("存在不包含的数字")
        value = input("请输入一个整数： ")
while len(vis) != n:
    quantity = random.randint(2,3)
    if quantity ==2:
        a = [random.randint(0,99),random.randint(0,99)]
    elif quantity == 3:
        a = [random.randint(0,99),random.randint(0,99),random.randint(0,99)]
    s = ''#以字符串的形式来存储题目
    ans = a[0]
    if len(a)==2:
        o = random.randint(0,1)
        if o == 0:
            ans+=a[1]
            s = f"{a[0]}+{a[1]}="
        else:
            ans-=a[1]
            s = f"{a[0]}-{a[1]}="
    else:
        oo = [random.randint(0,1),random.randint(0,1)]
        i = 1
        for o in oo:
            if o == 0:
                ans+=a[i]
            else:
                ans-=a[i]
            i+=1
        s = f"{a[0]}{operator[oo[0]]}{a[1]}{operator[oo[1]]}{a[2]}="
    if s not in vis and ans>= 0:#保证题目不会重复而且答案不会出现负数
        vis.append(s)
        answer.append(ans)
try:
    f1 = open("Exercises.txt",W)
    f2 = open("Answers.txt",W)
except File:
    print("数据写入错误")
for i in range(len(vis)):
    try:
        f1.write(str(i+1)+'. '+vis[i]+"\n")
        f2.write(str(i+1)+'. '+str(answer[i])+"\n")
    except File:
        print("数据写入错误！")
f1.close()
f2.close()
print(f"已生成{n}道题和答案到指定文件中！")


            
        
    
    


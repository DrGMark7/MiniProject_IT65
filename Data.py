#Discord_Name = ม.5 โช นภัสกร สงขลา
#Name = Napasskorn Saenieo 
#Email = chokun5588@gmail.com
#Class = ม.5

import time as t #* ดึง Library Time ตั้งชื่อเล่นว่า t
import sys

DataW = open('log.txt','a',encoding='utf-8') #* เปิดไฟล์ log.txt พร้อมเขียน
DataW.write(f'[{str(t.ctime())}] Start Program\n')

def Calculator(tense): #* สร้าง Function Calculator รับ Parameter เป็น tense หรือประโยค Input

    #* tense ใน dunction calculator จะเป็นการเล่น Index ของ List และตรวจสอบไปเรื่อย 
    tense = str(tense) #* แปลง Datatype ให้เป็น string เพื่อความมั้นใจ
    DataW.write(f'[{str(t.ctime())}] User Ask : {tense}\n')
    Tense = tense.split() #* แตก tense ให้เป็น List String    

    if Tense[1] == '+':
        Out = float(Tense[0]) + float(Tense[-1])
        DataW.write(f'[{str(t.ctime())}] Result : {str(Out)}\n')
    elif Tense[1] == '-':
        Out = float(Tense[0]) - float(Tense[-1])
        DataW.write(f'[{str(t.ctime())}] Result : {str(Out)}\n')
    elif Tense[1] == '*':
        Out = float(Tense[0]) * float(Tense[-1])
        DataW.write(f'[{str(t.ctime())}] Result : {str(Out)}\n')
    elif Tense[1] == '/':
        if (float(Tense[-1]) == 0):
            print("Cannot Division By Zero") #* Debug Error 0 ไม่สามารถหารได้
            sys.exit()
        Out = float(Tense[0]) / float(Tense[-1])
        DataW.write(f'[{str(t.ctime())}] Result : {str(Out)}\n')
    elif Tense[1] == '//':
        if (int(Tense[-1]) == 0):
            print("Cannot Division By Zero") #* Debug Error 0 ไม่สามารถหารได้
            sys.exit()
        Out = float(Tense[0]) // float(Tense[-1])
        DataW.write(f'[{str(t.ctime())}] Result : {str(Out)}\n')
    elif Tense[1] == '%':
        if (float(Tense[-1]) == 0):
            print("Cannot Modulo By Zero") #* Debug Error 0 ไม่สามารถmodด้
            sys.exit()
        Out = float(Tense[0]) % float(Tense[-1])
        DataW.write(f'[{str(t.ctime())}] Result : {str(Out)}\n')
    elif Tense[1] == '**':
        Out = float(Tense[0]) ** float(Tense[-1])
        DataW.write(f'[{str(t.ctime())}] Result : {str(Out)}\n')
    else:
        Out = 'Syntax Error'
        DataW.write(f'[{str(t.ctime())}] User input Error Cannot Result')

    return Out 

def ConTemp(tense): #* สร้าง Function ConTemp รับ Parameter เป็น tense หรือประโยค Input

    #// 25C = F
    #* tense ของ Function นี้จะเป็นการเล่น string ที่มี int อยู่ด้วยเป็นการเล่น datatype ครับ
    tense = str(tense) #* แปลง Datatype ให้เป็น string เพื่อความมั้นใจ
    Tense = tense.split() #* แตก tense ให้เป็น List String
    DataW.write(f'[{str(t.ctime())}] User Ask : {tense}\n')
    
    #* C Celsius
    if (Tense[0][-1] == 'C') and (Tense[-1]=='F'):
        C = float(Tense[0][:-1])
        F = 32 + ((9*C)/5)
    elif (Tense[0][-1] == 'C') and (Tense[-1]=='C'):
        C = float(Tense[0][:-1])
        C = C
    elif (Tense[0][-1] == 'C') and (Tense[-1]=='K'):
        C = float(Tense[0][:-1])
        K = C + 273
    elif (Tense[0][-1] == 'C') and (Tense[-1]=='R'):
        C = float(Tense[0][:-1])
        R = (4*C)/5
    
    #* F Fahrenheit
    if (Tense[0][-1] == 'F') and (Tense[-1]=='F'):
        F = float(Tense[0][:-1])
        F = F
    elif (Tense[0][-1] == 'F') and (Tense[-1]=='C'):
        F = float(Tense[0][:-1])
        C = ((F-32)/9)*5
    elif (Tense[0][-1] == 'F') and (Tense[-1]=='K'):
        F = float(Tense[0][:-1])
        K = (((F-32)/9)*5) + 273
    elif (Tense[0][-1] == 'F') and (Tense[-1]=='R'):
        F = float(Tense[0][:-1])
        R = (((F-32)/9)*4)
    
    #* K Kelvin
    if (Tense[0][-1] == 'K') and (Tense[-1]=='F'):
        K = float(Tense[0][:-1])
        F = (((K-273)/5)*9) + 32
    elif (Tense[0][-1] == 'K') and (Tense[-1]=='C'):
        K = float(Tense[0][:-1])
        C = K-273
    elif (Tense[0][-1] == 'K') and (Tense[-1]=='K'):
        K = float(Tense[0][:-1])
        K = K
    elif (Tense[0][-1] == 'K') and (Tense[-1]=='R'):
        K = float(Tense[0][:-1])
        R = (K-273)*0.8
    
    #* R Romer
    if (Tense[0][-1] == 'R') and (Tense[-1]=='F'):
        R = float(Tense[0][:-1])
        F = ((9*R)/4)+32
    elif (Tense[0][-1] == 'R') and (Tense[-1]=='C'):
        R = float(Tense[0][:-1])
        C = ((F-32)/9)*5
    elif (Tense[0][-1] == 'R') and (Tense[-1]=='K'):
        R = float(Tense[0][:-1])
        K = (((F-32)/9)*5) + 273
    elif (Tense[0][-1] == 'R') and (Tense[-1]=='R'):
        R = float(Tense[0][:-1])
        R = R
    

    #* บรรทัดที่ 121 - 131 เป็นการเขียนคล้ายๆกับ Switch case ในภาษา C 
    #* ผมยังไม่ลง 3.10 มาใช้ที่เห็นว่ามี Switch case แล้ว5555
    if Tense[-1] == 'C':
        Final = C
    elif Tense[-1] == 'F':
        Final = F
    elif Tense[-1] == 'K':
        Final = K
    elif Tense[-1] == 'R':
        Final = R
    else: 
        print("Syntax Error")
        DataW.write(f'[{str(t.ctime())}] User input Error Cannot Result')

    DataW.write(f'[{str(t.ctime())}] Result : {str(Final)}\n')
    print(f"Result : {Tense[0]} : {Final}°{Tense[-1]}")
      
print("============Hello World!============")
print("Select Menu for Quick Python Project")
print("------------------------------------")
print("1 : Calculator")
print("2 : Converter Temp")
print("3 : exit program")

Menu = str(input("Input Menu : "))

if Menu == '1':
    print("   Oparetor : + - * / // % **   ")
    print("--------------------------------")
    print("Input :  1 // 1")
    print("Output:  1.0 ")
    print("Type  :  'exit' for exit progarm")
    print("--------------------------------")
    while True:
        tense =  input("Calculate : ")
        if tense == 'exit':
            break
        print(f"Result : {Calculator(tense)}")
elif Menu == '2':
    print("C : Celsius , F : Fahrenheit")
    print("K : Kelvin  , R : Rømer")
    print("--------------------------------")
    print("Input : 25C = F")
    print("Output: 25C : 77F")
    print("Type  :  'exit' for exit progarm")
    print("--------------------------------")
    while True:
        tense =  input("ConvertTemp : ")
        if tense == 'exit':
            break
        ConTemp(tense)
elif Menu == '3':
    exit() #* จบการทำงานตัวโปรแกรมทันที
else :
    print("Not Found Menu") #* User Input Error

DataW.write('------------------------\n')
DataW.close() #* ปิดไฟล์ log.txt 
DataR = open('log.txt','r',encoding='utf-8') 
DataR.read()
DataR.close()
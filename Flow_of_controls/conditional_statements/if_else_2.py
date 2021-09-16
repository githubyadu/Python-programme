num1=int(input('enter no1'))
num2=int(input('enter no2'))
num3=int(input('enter no3'))
if num1>num2>num3:
    print('num1 is greater')
elif num2>num1>num3:
    print('num2 is greater')
elif num1==num2==num3:
    print('values are same')
else:
    print('num3 is greater')

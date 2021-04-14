try:
     a=int(input('number1'))
     b=int(input('number2'))
     c=a/b
     print(c)

except ValueError:
    print('输入错误')
except ZeroDivisionError:
    print('分母不能为零')

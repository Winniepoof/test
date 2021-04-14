# print('hello word');
# print(520);
# fp=open ('D:/TEXT.txt','a+')
# print('hello world',file=fp)
# fp.close()
# print('hello\tworld')
# print('hello\nworld')
# print(chr(0b100111001011000))
# print(ord('张'))
# name='张海迎'
# age=21
# print(type(name),type(age))
# print('我叫'+name+',今年'+str(age)+'岁')
# a1=121
# a2=2.1
# a3=True
# a4='123'
# print(int(a1),int(a2),int(a3),int(a4))
# print(str(a1),str(a2),str(a3),str(a4))
# print(float(a1))
#
# a=input('give me a namber1:')
# b=input('give me a namber2:')
# print(a+b)
# print(int(a)+int(b))
#
# a,b,c=10,20,30
# print(a==10 and b==20)
# print(a==10 and b==10)
# print(a==10 or b==10)
#
# a='helloworld' #判断字符串中是否存在某个字符串
# print('lol' in a)
#
# money=1000;
# s=int(input('金额为'))
# if money>=s:
#     money=money-s
#     print('余额为'+str(money))
#
# num=int(input('输入一个数'))
# if num%2==0:
#     print(num,'是偶数')
# else:
#     print(num,'是奇数')
#
# sum=0
# num=0
# while num<5:
#     sum+=num
#     num+=1
#     print(sum)
#
# for i in range(10):
#     pass
# print(i)

# for item in range(100,1000):
#     ge=item%10
#     shi=(item//10)%10
#     bai=item//100
#     #print(ge,shi,bai)
#     if ge*ge*ge+shi*shi*shi+bai*bai*bai==item:
#         print(item)


# for i in  range(3):
#     a = input('please enter your passworld:')
#     if a=='8888':
#         print('correct')
#         break
#     else:
#         print('incorrect')

# b=0
# while b<3:
#     a = input('please enter your passworld:')
#     if a == '8888':
#         print('correct')
#         break
#     else:
#         print('incorrect')
#     continue

# for i in range(1,4):
#     for j in  range(1,5):
#         print(str(i)+str(j),end='\t')#不换行输出
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,'*',j,'=',i*j,end='\t')
#     print()

abc=['hello','world', 123,1.2,123]
lst=[1.2,0.3]

print(lst)
print(abc.index(123,3,5))
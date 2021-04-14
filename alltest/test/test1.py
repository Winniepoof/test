lst=['zxl','lxn']
a='zxl'
for i in range(len(lst)):
    print(i,lst[i])

for i,item in enumerate(lst,1):
    print(i,item)

b=a[::-1]
print(b)

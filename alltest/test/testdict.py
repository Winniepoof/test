stu={'张海迎':21,'张海盐':120}
print(stu)
print(stu['张海盐'])
print(stu.get('张海迎'))
stu['张海客']=150
print(stu)

key=stu.keys()
print(key)
print(list(key))

value=stu.values()
print(list(value))

item=stu.items()
print(list(item))

for item in stu:
    print(item,stu.get(item))

names=['张海琪','张海虾','张海杏']
ages=[202,60,180]
zhang={name:age for name,age in zip(names,ages)}
print(zhang)
zhang.update(stu)
print(zhang)
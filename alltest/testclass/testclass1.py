class Student:
    place='吉林'
    def __init__(self,name,age):
        self.name=name
        self.age=age

stu1=Student('张三',20)
print(stu1.name)
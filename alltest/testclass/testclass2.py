class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f'我叫{self.name}，今年{self.age}岁')


class Student(Person):
    place='吉林'
    def __init__(self,name,age,numb):
        super().__init__(name,age)
        self.numb=numb
    def eat(self):
            print(self.name+'吃pi')
    def info(self):
        super().info()
        print(f'我的学号是{self.numb}')
    def __str__(self):
        return f'我叫{self.name}，今年{self.age}岁'

stu1=Student('张三',20,1001)
stu1.info()
print(stu1)
Student.eat(stu1)
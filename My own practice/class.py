class Student:
    name = None
    age = None
    def __init__(self,name,age):  #构造方法
        self.name = name
        self.age = age

    def hello(self, msg):                   
        print(f"hello, my name is {self.name},{self.age} years old， and {msg}")


stu = Student("dudu",18)
# stu.name = "dudu"
stu.hello("nice to meet you all!")

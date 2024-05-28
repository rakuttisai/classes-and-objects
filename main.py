class student:
    def __init__(self,name,rollnum,javamarks,pythonmarks,mathmarks):
        self.name = name
        self.rollnum = rollnum
        self.javamarks = javamarks
        self.pythonmarks = pythonmarks
        self.mathmarks = mathmarks
        
obj = student("kishore",501,67,52,42)
print(obj.name)
print(obj.rollnum)
print(obj.javamarks)
print(obj.pythonmarks)
print(obj.mathmarks)

obj2 = student("lakshman",550,60,56,45)
print(obj2.name)
print(obj2.rollnum)
print(obj2.javamarks)
print(obj2.pythonmarks)
print(obj2.mathmarks)

obj3 = student("sai",600,58,69,55)
print(obj3.name)
print(obj3.rollnum)
print(obj3.javamarks)
print(obj3.pythonmarks)
print(obj3.mathmarks)
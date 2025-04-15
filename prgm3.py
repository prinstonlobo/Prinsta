class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"MY name is {self.name} and i am {self.age} years 👋👋👋")
o=A("printon",23)
o.display()
print(getattr(o,"salary","NF"))
print(hasattr(o,"age"))

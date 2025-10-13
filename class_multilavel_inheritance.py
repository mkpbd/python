# ================== What is Multiple Inheritance? ===================
# Multiple inheritance is a type of inheritance where a single class can inherit attributes and methods from more than one parent class.
#  This can be used when you want to get the functionality of multiple classes into a single class. 
# The image below illustrates multiple inheritance −

class Father:
    def skill1(self):
        print("Father's skill: Gardening")

class Mother:
    def skill2(self):
        print("Mother's skill: Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()



##====================== multiple  inheritance =======================

class Father:
    def skill(self):
        print("Father's skill: Gardening")

class Mother:
    def skill(self):
        print("Mother's skill: Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill()


##======================= Using super() in Multiple Inheritance

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")
        super().show()

class C(A):
    def show(self):
        print("Class C")
        super().show()

class D(B, C):
    def show(self):
        print("Class D")
        super().show()

d = D()
d.show()
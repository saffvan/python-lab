from college_package import student
from college_package import staffs
from college_package.sub_package1.add import addition
from college_package.sub_package2.subtract import subtraction

x=int(input("enter a num1 : "))
y=int(input("enter a num2 : "))
addition(x,y)
subtraction(x,y)
student.stud()
staffs.staff()

from Graphics_package import circle,rectangle
from Graphics_package.ThreeD_graphics_sub_package.sphere import *
#from Graphics_package import circle
#from Graphics_package import rectangle
from Graphics_package.ThreeD_graphics_sub_package import cuboid
#from Graphics_package.ThreeD_graphics_sub_package import sphere

print("\n circle \n")
radius= int(input("enter a radius "))
circle.circle_area(radius)
circle.circle_perimeter(radius)

print("\n rectangle \n")
length= int(input("enter a length "))
height= int(input("enter a height "))
rectangle.area_rect(length,height)
rectangle.peremeter_rect(length,height)

print("\n cuboid \n")
length1= int(input("enter a length "))
breadth = int(input("enter a breadth "))
height1= int(input("enter a height "))
cuboid.perimeter_cuboid(length1, breadth, height1)
cuboid.area_cuboid(length1, breadth, height1)

print("\n sphere \n")
radius1= int(input("enter a radius "))
area_sphere(radius1)
perimeter_sphere(radius1)

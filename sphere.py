def sphere(radius):
    import math
    if isinstance(radius, (str, float)):
        print("error, not an integer")
    else:
        volume = (4/3)*math.pi*radius**3
        area = (4)*math.pi*radius**2
        print ("The volume of the sphere is: ")
        print (volume)
        print ("The surface area of the sphere is: ")
        print (area)
        
def rectPrism(length, width, height):
    import math
    if isinstance(length or width or height, (str, float)):
        print("error, one or more inputted values is not an integer")
    else:
        volume = length*width*height
        area = 2*length*width + 2*width*height + 2*length*height
        print ("The volume of the prism is : ")
        print (volume)
        print ("The surface area of the prism is: ")
        print (area)
        
def triPrism(length, width, height):
    import math
    if isinstance(length or width or height, (str, float)):
        print("error, one or more inputted values is not an integer")
    else:
        volume = (1/2)*length*width*height
        area = length*width + width*height + 2*length*(height**2+width**2)**.5
        print ("The volume of the prism is : ")
        print (volume)
        print ("The surface area of the prism is: ")
        print (area)
        
def cone(radius, height):
    import math
    if isinstance(radius or height, (str, float)):
        print("error, one or more inputted values is not an integer")
    else:
        volume = (1/3)*math.pi*height*radius**2
        area = math.pi*radius*(radius + (height**2+radius**2)**.5)
        print ("The volume of the cone is : ")
        print (volume)
        print ("The surface area of the cone is: ")
        print (area)
        
def cylinder(radius, height):
    import math
    if isinstance(radius or height, (str, float)):
        print("error, one or more inputted values is not an integer")
    else:
        volume = math.pi*height*radius**2
        area = 2*math.pi*radius*height + 2*math.pi*radius**2
        print ("The volume of the cylinder is : ")
        print (volume)
        print ("The surface area of the cylinder is: ")
        print (area)
        
def triPyramid(baseSide, height):
    import math
    if isinstance(baseSide or height, (str, float)):
        print("error, one or more inputted values is not an integer")
    else:
        volume = (1/3)*height*((3**.5)/2)*baseSide**2
        area = 3*(((((3**.5)/2)*baseSide)**2+height**2)**.5)*(1/2)*baseSide
        print ("The volume of the triangular pyramid is : ")
        print (volume)
        print ("The surface area of the triangular pyramid is: ")
        print (area)
        
def squarePyramid(baseSide, height):
    import math
    if isinstance(baseSide or height, (str, float)):
        print("error, one or more inputted values is not an integer")
    else:
        volume = (1/3)*height*baseSide**2
        area = 3*((1/2)*baseSide*(((1/2)*baseSide)**2+height**2)**.5)
        print ("The volume of the triangular pyramid is : ")
        print (volume)
        print ("The surface area of the triangular pyramid is: ")
        print (area)
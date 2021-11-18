# 1. Find Area
def room():
    while True:
        question = input(" Do you want to know your room's area? yes or no ")
        if question == 'no':
            print("You are no longer interested in finding the area.")
            break
        else:
            length = int(input("What is the length of the room? "))
            width = int(input("What is the width? "))
            area = length * width
            print("The area of the room is " + str(area))
            break
            
room()



# 2. Find Circumference
def circle():
    while True:
        question = input("Do you want to find out your circle's circumference? yes or no ")
        if question == 'no':
            print("You are no longer interested in finding the circumference.")
            break
        else:
            radius = int(input("What is the radius of the circle? "))
            pi = 3.14
            cirum = 2 * pi * radius
            print("The circumference of the circle is " + str(cirum))
            break

circle()
#usage of %d,%f,%s
#print ("uasge of %"%(args))
#prefer this for calculations processing and data handling

'''price = 49.99;grade = 'A'; stock = 1000
print("price is %f"%price)
print("grade is %s"%grade)
print("stock is %d"%stock)'''


'''radius = 3.5
area_of_circle = 3.1416 * radius * radius
print("area of circle is %.2f"%area_of_circle)'''

'''name = "codegnan";batch = "pfs6"
print(f'{batch} is in {name}')
print(f"sai is in {name}")'''

'''a,b = map(int,input("enter a values").split(','))
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
print("addition of two numbers:",addition)
print("subtraction of two numbers:",subtraction)
print("multiplication of two numbers:",multiplication)
print("division of two numbers:",division)
'''


#control block statements : they control the flow of the program
#conditional statements : if,if-else,if-elif-else
#relational operators : >,<,>=,<=,==,!= (loop) (for while)
#jump statements : break,continue,pass

'''
syntax for conditional statements:
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false

if-elif-else:
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
else:
    # code to execute if both conditions are false

if-else-if ladder:
if condition1: 
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
elif condition3:
    # code to execute if condition3 is true
else:
    # code to execute if all conditions are false

'''

#BMI :body mass index
weight = int(input("enter weight in kg: "))
height = float(input("enter height in meters: "))
bmi = weight / (height * height) 
print(bmi)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
else:
    print("bmi is in obese category")
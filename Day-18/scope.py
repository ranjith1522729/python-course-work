#Scope determines where a variable can be accessed within a program.
#A variable is only accessible within the region where it is defined.
'''
def display():
    print("Inside the Function: ",n)

n = 10
display()
print("Outside the function: ",n)

def display():
    global n
    n += 10
    print("Inside Function: ",n)


display()
print("Outside function: ",n)

#A variable declared outside all functions is called a global variable.
def display():
    global n 
    n+=10
    print("Inside the function: ",n)

n=10
display()
print("Outside function: ",n)

def display():
    course = "PFS"
    def update():
        nonlocal course
        course = 'JFS'
        print("Inner Function: ",course)
    update()
    print("Outer Function: ",course)

display()

l = [1,2,3,4,5]
print(max(l))

print = 20
print(max)
'''
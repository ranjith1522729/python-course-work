def table(n):
    print(f"{n}-Table")
    print('-------------')
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

for i in range (1,21):
    table(i)

def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

print(isleap(2012))
print(isleap(2014))
print(isleap(2026))

def is_prime(n):
    prime = False

    for i in range(1,n):
        if n % 1 == 0:
            prime = True
        else:
            prime = False

    return "Prime"

n = int(input("Enter the number: "))
prime(is_prime(n))

def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display(name='rasool',email='rasool@gmail.com',pwd='rasool@123')
display(email='rasool@gmail.com',name='rasool',pwd='rasool@123')
display(pwd='rasool@123',name='rasool',email='rasool@gmail.com')

def display(name,email,pwd=None):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display("rasool","email")
display("rasool","email","pwd@123")

def display (**names):
    print(names)

display(n1="rasool")
display(n1="rasool",n2="virat")
display(n1="rasool",n2="virat",n3="rohit")
display(n1="rasool",n2="virat",n3="rohit",n4="bhuvi")
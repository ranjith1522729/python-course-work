
'''
s = 'Ranjith Kumar'
for i in s:
    print(i)

l = [1,2,3,4,5]
for num in l:
    print(num)

prices = (9876,7654,543,432,321)
for price in prices:
    print(price)

names = {'Ranjith Kumar','Rasool','vardhan'}
for name in names:
    print(name)

d = {1:2,2:4,3:6,4:8,5:10}
for i in d:
    print(i,d[i])

#range(start,end+1,step):(0,,1)
for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(5,0,-1):
    print(i)

for i in range(19,0,-2):
    print(i)

s = 'Ranjith Kumar Yaramothu'
for i in range(len(s)):
    print(i,s[i])

s= ['987','654','432','432','321']
for i in range(len(s)):
    print(i,s[i])

s = ('Ranjith Kumar Yaramothu')
for i in enumerate(s):
    print(i,i[0],i[1])

d = {1:2,2:4,3:6,4:8,5:10}
for i in enumerate (d):
    print(i[0],i[1],d[i[1]])

for i in range(1,111):
    if i==5:
        break
    print(i)

for i in range(1,111):
    if i==5:
        continue
    print(i)

for i in range(1,11):
    if i==15:
        break
        print(i)
else:
    print("End of the Loop")

l = [12,13,15,16,18,19]
n=26
for i in l:
    if i==n:
        break
        print(n, "Found")
        break
else:
    print(n, "Not Found")

pin = 12345
for i in range(5):
    epin = int(input("Enter the pin: "))
    if epin == pin:
        print("unlock successful")
        break
    else:
        print("Incorrect pin")
else:
    print("Try after the 1 hour")
'''
n = 14
for i in range(2,n//2+1):
    if n%i == 0:
        print("Not a prime number")
        break
    else:
        print("Prime number")


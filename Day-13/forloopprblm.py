'''
n = int(input("Enter the input: "))
res = []
for i in range(1,n+1):
    if n%i == 0:
        res.append(i)

print(f'Factors of {n} = {res}')

s = 'Python Programming'
d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
        {'p':2,'y':1,'t':1,'h':1,'o':2','n':2,' ':1,'r':2,'g':2,'m':2,'i':1}
print(d)

s = 'aaaaaabbbbbccccddddeeee'
c=1
res = ''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        res+= s[i]+str(c) 
        c=1
print(res+s[-1]+str(c))
'''

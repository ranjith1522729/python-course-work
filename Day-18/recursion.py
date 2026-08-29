#recursion 
#function calling recursion itself
#until unless we a stopping condition base is applied
'''
def function():
if base_condition:
return
function()

def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)

def display(n):
    if n==0:
        return
    print(n)
    display(n-1)
display(10)
'''
def display(s,n):
    if n==len(s):
        return
    print(s[n])
    display(s,n+1)

display("Python",0)
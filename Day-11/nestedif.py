'''
fa = eval(input("Follows Account: "))
if fa:
    cf = eval(input("Close Friend: "))
    if cf:
        print("Visible story")
else:
    print("Follow the account")


reg = eval(input("Registered: "))
if reg:
    fee = (input("Fees paid: "))
    if fee:
        print("Tournament entry confirmed")
    else:
        print("Fees not paid")
else:
    print("SIGN UP FIRST")
'''
  
data = {
    'Ranjith Kumar':{'status':True,'python':97,'mysql':98,'Flask':96},
    'Rasool':{'status':True,'python':95,'mysql':96,'Flask':98},
    'Dinesh':{'status':True,'python':77,'mysql':88,'Flask':96},
    'Dipak':{'status':False,'python':None,'mysql':None,'Flask':None},
    'vardhan':{'status':True,'python':87,'mysql':88,'Flask':86},
}
name = input("Enter the name: ")
if name in data:
    if data[name]['status']:
        sum = data[name]['python']+data[name]['mysql']+data[name]['Flask']
        avg = sum/3
        print(f"Hello {name}!!!")
        print(F"Your average score is {avg}")
        if avg >= 90:
            print("Outstanding Performance")
        elif avg >= 80:
            print("Very Good, Keep Going")
        elif avg >= 70:
            print("Good, Try to work Harder")
        elif avg >= 60:
            print("Okay, keep Trying")
    else:
        print("You Failed in the exam, Better Luck Next Time, bring your parents to the school")
    


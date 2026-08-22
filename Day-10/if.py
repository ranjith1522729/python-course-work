
sales = int(input("enter the sales:"))

if sales > 1000:
    print("Best seller of the month")

eli_acc = eval(input("eligible Account: "))
ver_sub = eval(input("Meta Verified Subscription: "))

if eli_acc and ver_sub:
     print("verified Badge Granted")

rain_status = input("Is it raining? (yes/no): ")
if rain_status == "yes": 
    print("Carry an umbrella")
else:
    print("No need for an umbrella")


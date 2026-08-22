Units = int(input("Enter the Units: "))
Senior_citizen = eval(input("Are you a senior citizen? (True/False): "))

if Units <= 100 and Senior_citizen:
     bill_amount = (Units * 1.5) - (Units * 1.5 * 0.1)  # 10% discount for senior 
else:
    bill_amount = (Units * 1.5)
if Units <= 200 and Units >= 101 and Senior_citizen:
    bill_amount = (Units * 2.5) - (Units * 2.5 * 0.1)  # 10% discount for senior
else:
    bill_amount = (Units * 2.5)
if Units <= 500 and Units >= 201 and Senior_citizen:
    bill_amount = (Units * 4) - (Units * 4 * 0.1)  # 10% discount for senior
else:
    bill_amount = (Units * 4)
if Units > 500 and Senior_citizen:
    bill_amount = (Units * 6) - (Units * 6 * 0.1)  # 10% discount for senior
else:
    bill_amount = (Units * 6)
    
if Units > 800:
 bill_amount = bill_amount + (Units * 0.5)
else:
    bill_amount = bill_amount
print("Your electricity bill amount is: ", bill_amount)


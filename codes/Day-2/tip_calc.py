print('Welcome to the tip Calc!!')

bill = float(input())
tip = float(input())
people = int(input())
bill_with_tip = bill * (1 + tip/100)
bill_per_person = round((bill_with_tip / people), 2)
print(f"Each person should pay {bill_per_person}")

#What was the total bill?
#What percentage tip would you like to give? 10, 12, or 15?
#How manu people to split the bill?
#Each person should pay:
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How manu people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
#How to round to 2 decimal places?
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
#another way to do this exercize
#bill_with_tip = tip / 100 * bill + bill
#print(bill_with_tip)

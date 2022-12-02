# .............project-2:tip-calculator...................
print("Welcome to the tip calculator")
total_Bill = float(input("what was the total bill?\n"))
tip = int(
    input("what percentage tip would you like to give? 10, 12,, or 15?\n"))
final_bill = (tip/100 * total_Bill) + total_Bill
people = int(input("how many people to split the bill?\n"))
each_pay = round(final_bill / people, 2)
print(f"Each person should pay ${each_pay}")

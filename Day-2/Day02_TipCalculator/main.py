# Tip Calculator - Day 2 Project

print("Welcome to the Tip Calculator! 💰")

# 1. Get the total bill amount
bill = float(input("What was the total bill? ₹"))

# 2. Ask for the tip percentage
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# 3. Ask how many people are splitting the bill
people = int(input("How many people to split the bill? "))

# 4. Calculate the bill with tip
tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount

# 5. Divide the bill per person
bill_per_person = total_bill / people

# 6. Round the result to 2 decimal places
final_amount = round(bill_per_person, 2)

# 7. Use f-string to display result
print(f"Each person should pay: ₹{final_amount}")

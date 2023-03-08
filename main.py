
age = input("What is your current age? ")

years_rem = 90 - int(age)

days_rem = years_rem * 365

weeks_rem = years_rem * 52

months_rem = years_rem * 12

print(f"You have {days_rem} days, {weeks_rem} weeks and {months_rem} months left")
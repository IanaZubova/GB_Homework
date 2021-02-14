from sys import argv

script_name, hours, hours_pay, bonus = argv

hours = int(hours)
hours_pay = int(hours_pay)
bonus = int(bonus)

def salary():
    return ((hours * hours_pay) + bonus)

print("Script name: ", script_name)
print("Hours: ", hours)
print("Pay per hour: ", hours_pay)
print("Bonus: ", bonus)
print("Salary: ", salary())
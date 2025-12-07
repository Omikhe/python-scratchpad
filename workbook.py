calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_hours } {name_of_unit}"
    elif num_of_days == 0:
        return "0 days?, really?"
    else:
        return "you entered a negative value"

user_input = int(input("Enter number of days\n"))
data = days_to_units(user_input)
print(data)


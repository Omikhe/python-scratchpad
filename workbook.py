calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_hours } {name_of_unit}"
    elif num_of_days == 0:
        return "0 days?, really?"
    else:
        return "you entered a negative value"

user_input = input("Enter number of days\n")

if user_input.isdigit():
    user_input_number = int(user_input)
    data = days_to_units(user_input_number)
    print(data)
else:
    print("that's not a number!")

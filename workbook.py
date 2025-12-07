calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_hours } {name_of_unit}"
    

def validate_and_execute():

    #check if num is a digit
    if user_input.isdigit():
        user_input_number = int(user_input)

        #check if num is positive
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("0 days?, really?")
        else:
            print("you entered a negative value")
        
    else:
        print("that's not a number!")

user_input = input("Enter number of days\n")
validate_and_execute()

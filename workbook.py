calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_hours } {name_of_unit}"
    

def validate_and_execute():

    #check if num is a digit
    try:
        user_input_number = int(number_of_days_element)

        #check if num is positive
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("0 days?, really?")
        else:
            print("you entered a negative value")
        
    except ValueError:
        print("that's not a valid number!")

user_input = " "
while user_input != "exit":
    user_input = input("Enter number of days\n")
    for number_of_days_element in set(user_input.split()):
        validate_and_execute()

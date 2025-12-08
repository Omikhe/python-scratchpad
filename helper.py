def days_to_units(num_of_days, conversion_unit):
        if conversion_unit == "hours":
            return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
        elif conversion_unit == "minutes":
            return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}"
        elif conversion_unit == "seconds":
            return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} {conversion_unit}"
        else:
            return "unsupported unit"
    

def validate_and_execute(days_and_unit_dictionary):

    #check if num is a digit
    try:
        user_input_number = int(days_and_unit_dictionary["days"])

        #check if num is positive
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("0 days?, really?")
        else:
            print("you entered a negative value")
        
    except ValueError:
        print("that's not a valid number!")


user_input_message = "Enter number of days and conversion unit\n"
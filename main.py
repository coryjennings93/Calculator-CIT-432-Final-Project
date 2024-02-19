from calculator import Calculator
import settings
from menu_display import MenuDisplay
from validation import Validation

def main():
    
    # Create an instance of the Calculator class`
    calculator = Calculator()

    # this variable is used to perform operations on the output
    # of the previous operation
    current_calculated_value = 0

    # Displays the menu
    MenuDisplay.display_menu()

    # Gets the menu choice from the user
    choice = input('Select the calculation to perform: ')

    # Make sure menu choice is valid option
    choice = Validation.validate_menu_choice(choice)
    

    
    while choice != settings.QUIT:

        # Square root is a separate type of function because it only requires 1 value to work   
        if choice == settings.SQROOT:
            x = input('What number do you want the square root of: ')
            # validate that x is a number
            x = Validation.validate_numeric_input(x)
            x = float(x)
            current_calculated_value = calculator.sqroot(x)

        else:

            # Get the numbers needed for the calculation from the user
            x, y = calculator.get_numbers()


            # Perform the calculation with the selected menu option and the two values and
            # save it as the current value
            current_calculated_value = calculator.perform_calculation(choice, x, y)

        choice = calculator.operate_on_current_value(current_calculated_value)
        


# Call the main function.
if __name__ == '__main__':
     main()
import os
from validation import Validation
import settings
from menu_display import MenuDisplay

class Calculator:

    def add(self, x, y):
        answer = x + y
        print(x, '+', y, '=', answer)
        self.copy_results_to_clipboard(answer)
        return answer

    def sub(self, x, y):
        answer = x - y
        print(x, '-', y, '=', answer)
        self.copy_results_to_clipboard(answer)
        return answer

    def mult(self, x, y):
        answer = x * y
        print(x, '*', y, '=', answer)
        self.copy_results_to_clipboard(answer)
        return answer

    def divide(self, x, y):
        # check to see if divisor value is 0
        while y == 0:
            print('Cannot divide by 0')
            y = input('Re-enter divisor value: ')
            # validate input data
            y = Validation.validate_numeric_input(y)

        answer = x / y
        print(x, '/', y, '=', answer)
        self.copy_results_to_clipboard(answer)
        return answer

    def sqroot(self, x):
        while True:
            try:
                get_sqroot = float(x)
                break
            except:
                print('Value was not a number')
                input('Enter numeric value: ')
                # validate value
                get_sqroot = Validation.validate_numeric_input(get_sqroot)
        # error check for negative number
        while get_sqroot < 0:
            print()
            print("Cannot take the square root of a negative number.")
            print("Current calculated value will reset.")
            print()
            get_sqroot = input("Enter positive value: ")
            # validate value
            get_sqroot = Validation.validate_numeric_input(get_sqroot)

        answer = get_sqroot**(1/2.0)
        print('Square root of', get_sqroot, 'is', answer)
        self.copy_results_to_clipboard(answer)
        return answer
    
    def perform_calculation(self, choice, x, y):
        if choice == settings.ADD:
            current_calculated_value = self.add(x, y)
            print()
            return current_calculated_value
        elif choice == settings.SUBTRACT:
            current_calculated_value = self.sub(x, y)
            print()
            return current_calculated_value
        elif choice == settings.MULTIPLY:
            current_calculated_value = self.mult(x,y)
            print()
            return current_calculated_value
        elif choice == settings.DIVIDE:
            current_calculated_value = self.divide(x,y)
            print()
            return current_calculated_value
        elif choice == settings.SQROOT:
            current_calculated_value = self.sqroot()
            print()
            return current_calculated_value

    def operate_on_current_value(self, current_calculated_value):
        # This loop checks to see if the user wants to perform an operation on the
        # previously calculated value
        while True:
            keep_current_value = input('Do you want to perform calculation on output value? \n' +
                                       'Enter y / n: ')
            Validation.validate_yes_or_no(keep_current_value)
            if keep_current_value.upper() == 'Y':
                MenuDisplay.display_menu()
                print('The current value is', current_calculated_value)
                print()
                choice = input('Enter operation to be performed on the current value: ')
                choice = Validation.validate_menu_choice(choice)
                
                if choice == settings.SQROOT:
                    current_calculated_value = self.sqroot(current_calculated_value)
                    print(current_calculated_value)
                elif choice == settings.QUIT:
                    return choice
                else:
                    second_number = input('Enter the second number: ')

                    # validate that the second_number is numeric input
                    second_number = Validation.validate_numeric_input(second_number)

                    # perform calculation and assign it as the current value
                    current_calculated_value = self.perform_calculation(choice, current_calculated_value, second_number)

                                
            elif keep_current_value.upper() == 'N':
                current_calculated_value = 0
                new_calc = input('Do you want to perform another calculaiton? \nEnter y / n: ')

                # validates input data for y or n value
                new_calc = Validation.validate_yes_or_no(new_calc)

                if new_calc.upper() == 'Y':
                    MenuDisplay.display_menu()
                    choice = input('Select the calculation to perform: ')
                    choice = Validation.validate_menu_choice(choice)
                    return choice
                elif new_calc.upper() == 'N':
                    choice = settings.QUIT
                    return choice
                else:
                    print('Invalid choice.')
                            
                                   
                
            else:
                print('Invalid choice.')

    def get_numbers(self):
        first_number = input('Enter the first number: ')
        
        # validate that first_number is numeric input
        first_number = Validation.validate_numeric_input(first_number)

        # convert first_number to float
        first_number = float(first_number)

        
        second_number = input('Enter the second number: ')
        
        # validate that the second_number is numeric input
        second_number = Validation.validate_numeric_input(second_number)

        #convert second_number to float
        second_number = float(second_number)
        
        return first_number, second_number

    def copy_results_to_clipboard(self, current_value):
        command = 'echo ' + str(current_value).strip() + '| clip'
        os.system(command)
        print()
        print('Results copied to clipboard')
        print()
    
            
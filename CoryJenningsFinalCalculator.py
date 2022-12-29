import os

# These are constants for the Menu values
ADD = 1
SUBTRACT = 2
MULTIPLY = 3
DIVIDE = 4
SQROOT = 5
QUIT = 6



def main():

    # this variable is used to perform operations on the output
    # of the previous operation
    current_calculated_value = 0

    # Displays the menu
    display_menu()

    # Gets the menu choice from the user
    choice = input('Select the calculation to perform: ')

    # Make sure menu choice is valid option
    choice = validate_menu_choice(choice)
    

    
    while choice != QUIT:

        # Square root is a separate type of function because it only requires 1 value to work   
        if choice == SQROOT:
            x = input('What number do you want the square root of: ')
            # validate that x is a number
            x = validate_numeric_input(x)
            x = float(x)
            current_calculated_value = sqroot(x)

        else:

            # Get the numbers needed for the calculation from the user
            x, y = get_numbers()


            # Perform the calculation with the selected menu option and the two values and
            # save it as the current value
            current_calculated_value = perform_calculation(choice, x, y)


        # This loop checks to see if the user wants to perform an operation on the
        # previously calculated value
        while True:
            keep_current_value = input('Do you want to perform calculation on output value? \n' +
                                       'Enter y / n: ')

            if keep_current_value.upper() == 'Y':
                display_menu()
                print('The current value is', current_calculated_value)
                print()
                choice = input('Enter operation to be performed on the current value: ')
                choice = validate_menu_choice(choice)
                
                if choice == SQROOT:
                    current_calculated_value = sqroot(current_calculated_value)
                    print(current_calculated_value)
                elif choice == QUIT:
                    break
                else:
                    second_number = input('Enter the second number: ')

                    # validate that the second_number is numeric input
                    second_number = validate_numeric_input(second_number)

                    # perform calculation and assign it as the current value
                    current_calculated_value = perform_calculation(choice, current_calculated_value, second_number)

                                
            elif keep_current_value.upper() == 'N':
                current_calculated_value = 0
                new_calc = input('Do you want to perform another calculaiton? \nEnter y / n: ')

                # validates input data for y or n value
                new_calc = validate_new_calc(new_calc)

                if new_calc.upper() == 'Y':
                    display_menu()
                    choice = input('Select the calculation to perform: ')
                    choice = validate_menu_choice(choice)
                    break
                elif new_calc.upper() == 'N':
                    choice = QUIT
                    break
                else:
                    print('Invalid choice.')
                            
                                   
                
            else:
                print('Invalid choice.')


                  
    
def display_menu():
    print()
    print('Please pick a calculation')
    print('---------------------------')
    print('(1) for Addition')
    print('(2) for Subtraction')
    print('(3) for Multiplication')
    print('(4) for Division')
    print('(5) for the Square Root')
    print('(6) to QUIT')
    print('---------------------------')


def get_numbers():
    first_number = input('Enter the first number: ')
    
    # validate that first_number is numeric input
    first_number = validate_numeric_input(first_number)

    # convert first_number to float
    first_number = float(first_number)

    
    second_number = input('Enter the second number: ')
    
    # validate that the second_number is numeric input
    second_number = validate_numeric_input(second_number)

    #convert second_number to float
    second_number = float(second_number)
    
    return first_number, second_number


def add(x, y):
    answer = x + y
    print(x, '+', y, '=', answer)
    copy_results_to_clipboard(answer)
    return answer

def sub(x, y):
    answer = x - y
    print(x, '-', y, '=', answer)
    copy_results_to_clipboard(answer)
    return answer

def mult(x,y):
    answer = x * y
    print(x, '*', y, '=', answer)
    copy_results_to_clipboard(answer)
    return answer

def divide(x,y):
    # check to see if divisor value is 0
    while y == 0:
        print('Cannot divide by 0')
        y = input('Re-enter divisor value: ')
        # validate input data
        y = validate_numeric_input(y)

    answer = x / y
    print(x, '/', y, '=', answer)
    copy_results_to_clipboard(answer)
    return answer


def sqroot(x):
    while True:
        try:
            get_sqroot = float(x)
            break
        except:
            print('Value was not a number')
            input('Enter numeric value: ')
            # validate value
            get_sqroot = validate_numeric_input(get_sqroot)
    # error check for negative number
    while get_sqroot < 0:
        print()
        print("Cannot take the square root of a negative number.")
        print("Current calculated value will reset.")
        print()
        get_sqroot = input("Enter positive value: ")
        # validate value
        get_sqroot = validate_numeric_input(get_sqroot)

    answer = get_sqroot**(1/2.0)
    print('Square root of', get_sqroot, 'is', answer)
    copy_results_to_clipboard(answer)
    return answer
        

def validate_menu_choice(choice):
    while True:
        try:
            choice = int(choice)
            while choice < 0 or choice > 6:
                choice = int(input('Please enter a valid menu choice: '))
            return choice
            break

        except:
            choice = input('Enter a valid numeric menu choice: ')

def perform_calculation(choice, x, y):
        if choice == ADD:
            current_calculated_value = add(x, y)
            print()
            return current_calculated_value
        elif choice == SUBTRACT:
            current_calculated_value = sub(x, y)
            print()
            return current_calculated_value
        elif choice == MULTIPLY:
            current_calculated_value = mult(x,y)
            print()
            return current_calculated_value
        elif choice == DIVIDE:
            current_calculated_value = divide(x,y)
            print()
            return current_calculated_value
        elif choice == SQROOT:
            current_calculated_value = sqroot()
            print()
            return current_calculated_value

def copy_results_to_clipboard(current_value):
    command = 'echo ' + str(current_value).strip() + '| clip'
    os.system(command)
    print()
    print('Results copied to clipboard')
    print()
    

def operate_on_current_value(current_calculated_value):
    print('operate_on_current_value')

def validate_numeric_input(num):
    while True:
        try:
            num = float(num)
            return num
            break
        except:
            print('Input is not a numeric value.')
            num = input('Enter numeric value: ')

def validate_new_calc(new_calc):
    if new_calc.upper() == 'Y':
        return 'Y'

    elif new_calc.upper() == 'N':
        return 'N'
    
    else:
        while True:
            new_calc = input("Please enter 'y' or 'n': ")
            if new_calc.upper() == 'Y':
                return 'Y'

            elif new_calc.upper() == 'N':
                return 'N'
        
        

# Call the main function.
if __name__ == '__main__':
     main()


    

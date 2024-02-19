class Validation:
    @staticmethod
    def validate_menu_choice(choice):
        while True:
            try:
                choice = int(choice)
                if choice >= 0 and choice <= 6:
                    return choice
                raise ValueError("Invalid input.")
            except ValueError as e:
                print(e)
                choice = input("Enter a valid numeric menu choice: ")

    @staticmethod
    def validate_numeric_input(num):
        while True:
            try:
                num = float(num)
                return num
            except ValueError:
                print('Input is not a numeric value.')
                num = input('Enter numeric value: ')
    
    @staticmethod
    def validate_yes_or_no(value):
        while True:
            try:
                if value.upper() in ('Y', 'N'):
                    return value.upper()
                raise ValueError("Invalid input.")
            except ValueError as e:
                print(e)
                value = input("Please enter 'Y' or 'N': ")
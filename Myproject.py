def calculate():
    operation = input('''
Please Type the math operation you would like to complete:
+ for addition
- for Subtraction
* for Multiplication
/ for division
''')

    number_1 = float(input('Please enter the First number: '))
    number_2 = float(input('Please enter the Second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have entered a wrong math operator!')
    again()

def again():
    calculation_again = input('''
Do you want to Calculate again?
Please type Y for Yes or N for No
''')

    if calculation_again.upper() == 'Y':
        calculate()
    elif calculation_again.upper() == 'N':
        print('Bye Bye, thank you for coming.')
    else:
        again()

calculate()

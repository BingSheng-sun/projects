# 本项目专注于使用python开发一个简单的计算器，我将会尽可能集成市面上主流计算器都有的功能，但是我可能不会设计开发优美的GUI界面，因为我认为命令行界面更加直观，此外，这个项目的目标是学习python，而不是开发一个完整的应用。

import calculate_functions

def get_numbers():
    try:
        numbers = input('Enter numbers separated by space: ').split()
        return [float(num) for num in numbers]
    except ValueError:
        print('Invalid input! Please enter numeric values.')
        return None
    
def format_result(result):
    if isinstance(result, int) or (isinstance(result, float) and result.is_integer()):
        return int(result)
    else:
        return result
    
def handle_calculation(operation, numbers):
    if numbers is None:
        return
    try:
        if operation == '1':
            result = calculate_functions.add(*numbers)
            print('The result of additionis:', format_result(result))
        elif operation == '2':
            result = calculate_functions.subtract(*numbers)
            print('The result of subtraction is:', format_result(result))
        elif operation == '3':
            result = calculate_functions.multiply(*numbers)
            print('The result of multiplication is:', format_result(result))
        elif operation == '4':
            result = calculate_functions.divide(*numbers)
            print('The result of division is:', format_result(result))
        elif operation == '5':
            if len(numbers) != 2:
                print('Invalid input! Please enter two numbers.')
                return
            try:
                m = int(numbers[0])
                n = int(numbers[1])
                result = calculate_functions.cmn(m, n)
                print(f'Cmn({m}, {n}) = {result}')
            except (ValueError, TypeError) as e:
                print(f"输入错误：{e}")
        elif operation == '6':
            result = calculate_functions.gcd(*numbers)
            print(f'The greatest common divisor of {numbers} is: {result}')
        elif operation == '7':
            result = calculate_functions.lcm(*numbers)
            print(f'The least common multiple of {numbers} is: {result}')
    except ZeroDivisionError:
        print('Invalid input! Please enter non-zero numbers.')

def main():
    print('-' *20)
    print('Welcome to the Simple Calculator')
    print('I\'m Xinyuan. This is my first python project, so it may not be perfect.' \
    'I want this project can help me to learn python and practice my programming skills.')
    print('0.1 Version: begin at 2025-12-21. In this version, it only supports basic arithmetic operations.')
    print('-' *20)

    while True:
        print('Please enter your operation(simple operatations for two numbers only):')
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. Cmn')
        print('6. 最大公约数')
        print('7. 最小公倍数')
        print('10. Exit')
        choice = input('Your choice: ')

        if choice =='10':
            print('Thank you for using my calculator. Goodbye!')
            break
        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            numbers = get_numbers()
            handle_calculation(choice, numbers)
        else:
            print('Invalid input! Please enter a valid choice.')

if __name__ == '__main__':
    main()
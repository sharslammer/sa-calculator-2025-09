import calculator

calc_functions = {
}

try:
    calc_functions['+'] = calculator.sum
    print('sum loaded')
except AttributeError:
    print('sum was not loaded')
try:
    calc_functions['-'] = calculator.substraction
except AttributeError:
    print('substraction was not loaded')
try:
    calc_functions['*'] = calculator.multiplication
except AttributeError:
    print('multiplication was not loaded')
try:
    calc_functions['/'] = calculator.division
except AttributeError:
    print('multiplication was not loaded')
try:
    calc_functions['//'] = calculator.division_without_remainder
except AttributeError:
    print('reminder was not loaded')
try:
    calc_functions['%'] = calculator.reminder
except AttributeError:
    print('reminder was not loaded')
try:
    calc_functions['^'] = calculator.exponentiation
except AttributeError:
    print('exponentiation was not loaded')
try:
    calc_functions['max'] = calculator.maximum
except AttributeError:
    print('maximum was not loaded')
try:
    calc_functions['min'] = calculator.minimum
except AttributeError:
    print('minimum was not loaded')


if __name__ == '__main__':
    while True:
        user_input = input('->')
        result = None
        for k, v in calc_functions.items():
            if k in user_input:
                a, b = [int(item) for item in user_input.split(k)]
                result = v(a, b)
                print(v(a, b))
        if not result:
            print('Invalid operation. Try again')
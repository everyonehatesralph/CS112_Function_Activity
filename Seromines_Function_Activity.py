num1 = int(input('Enter first number: ').strip())
num2 = int(input('Enter second number: ').strip())
num3 = int(input('Enter third number: ').strip())


def ralph_gwapo(first, second, third):
    if num1 == num2 == num3:
        return f"{first * second * third}"
    elif num1 == num2 != num3:
        return f"{first * second + third}"
    elif num2 == num3 != num1:
        return f"{second * third + first}"
    elif num1 == num3:
        return f"{first * third + second}"
    else:
        return f"{first + second + third}"


result = ralph_gwapo(num1, num2, num3)

print(f'The result is {result}.')



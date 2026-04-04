# try: 
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ZeroDivisionError:
#     print('You cannot divide by zero!')
# except ValueError:
#     print('Enter only a number')
# finally:
#     print("Calculation finished :) ")

# try:
#     f = open('forest.txt', 'r')
#     content = f.read()
#     lines = content.splitlines()
#     for line in lines:
#         if 'animal' in line and not 'not an animal' in line:
#             print(line)
#     # print(content)
# except FileNotFoundError:
#     print('File not found')
# finally:
#     print("Closing file...")
#     if f:
#         f.close()

def sum(f, s):
    res = f + s
    return res

def subtract(f ,s):
    res = f - s
    return res

def multiplic(f, s):
    res = f * s
    return res 

def divide(f, s):
    res = f / s
    return res

try:
    raw_val1 = input('First value: ')
    raw_val2 = input('Second value: ')
    operator = input('Type operator (+, -, *, /): ')

    if operator.isdigit():
        raise ValueError('operator cannot be a number!')

    if raw_val1.isalpha() or raw_val2.isalpha():
        raise ValueError('value cannot be a string!')

    val1 = int(raw_val1)
    val2 = int(raw_val2)

    if operator == '+':
        print(sum(val1, val2))
    elif operator == '-':
        print(subtract(val1, val2))
    elif operator == '*':
        print(multiplic(val1, val2))
    elif operator == '/':
        print(divide(val1, val2))
    else:
        print('error!')
except ZeroDivisionError:
    print('You cannot divide by zero!')
except ValueError as e:
    print('Value error! ', e)
finally:
    print('Calculation finished!')
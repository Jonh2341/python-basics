import math
import random

# print(math.sqrt(25))
# print(math.factorial(5))
# print(math.pow(5,2))
# print(math.log(100, 10))
# print(math.pi)
# print(math.e)

# bag = ['apple', 67, 'Kiwi', "Banana"]

# print(random.randint(1, 10))
# print(random.choice(bag))
# # print(random.random())
# random.shuffle(bag)
# print(bag)

try:
    val1 = int(input('min num: '))
    val2 = int(input('max num: '))

    rand_value = random.randint(val1, val2) 

    if rand_value % 2 == 0:
        math_sqrt = math.sqrt(rand_value)

        if math_sqrt.is_integer():
            math_sqrt = int(math_sqrt)
            print(f'random number is: {rand_value}; the square of this number is: {math_sqrt}')
        else:
            print(rand_value)
    else:
        print(rand_value)

except ValueError:
    print('only numbers!')
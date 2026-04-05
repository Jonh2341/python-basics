def add_something(func):
    def wrapper(*args, **kwards):
        # define addition
        addition = args[0] if args[0] != '' else 'standart'

        # exception for digits
        if any(char.isdigit() for char in addition):
            raise ValueError('Digits are not allowed!')

        # checking the addition ingridient
        if addition == 'standart':
            print('you add nothing')
        else:
            print(f'you add some {addition}')
        return func(addition, *args[1:], **kwards)
    return wrapper

# decorator
@add_something
def pasta(condition):
    print(f'there is your {condition} pasta!')

pasta('')
def add_something(func):
    def wrapper(*args, **kwards):
        addition = args[0] if args[0] != '' else 'standart'
        if addition == 'standart':
            print('you add nothing')
        else:
            print(f'you add some {addition}')
        return func(addition, *args[1:], **kwards)
    return wrapper

@add_something
def pasta(condition):
    print(f'there is your {condition} pasta!')

pasta('')
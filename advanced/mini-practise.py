import time

def get_fibonacci_time(func):
    def wrapper(*args, **kwards):
        def generator_wrap():
            start_time = time.perf_counter()
            
            for value in func(*args, **kwards):
                yield value

            end_time = time.perf_counter()
            duration = end_time - start_time
            print(f'done in {duration:.6f} seconds')
        return generator_wrap()
    return wrapper

@get_fibonacci_time
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b  

for num in fibonacci(10):
    print(num)
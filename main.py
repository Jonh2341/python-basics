# lists basics
favorite_movies = ["Don Juan", "Jack Sparrow", "Alice in Wonderland"]
favorite_movies.append("Finding Neverland")
print(favorite_movies)
favorite_movies.remove("Jack Sparrow")
print(favorite_movies)
print(favorite_movies[-1])

# tuples
fruits = ("apple", "banana", "mango", "lemon", "dragon fruit")

    # index
print(fruits[0])
print(fruits[-1])
    # slicing
print(fruits[1:4])

levels_one = (1, 5, 10, 7)
levels_two = (2, 4, 12, 15)

    # concatenation
print(levels_one + levels_two)
    # repetition 
print(levels_two * 2)
    # memberwhip
cars = ("Toyota", "Subaru", "Bugatti")

print("Bugatti" in cars)
print("BMW" in cars)

    # Length
print(len(cars))
    # Count occurences
data = (1, 2, 2, 3, 1, 5, 5, 6, 5, 9)
print(data.count(5))

    # tuple can't be modified after creation
autors = ("Bob", "John", "Jack")
    # autors[0] = "Zack" --> error 

    # list can be modified
coworkers = ["Jack", "John", "Zack"]
coworkers[0] = "Johnny"
# --> no error
print(coworkers)

    # unpacking
age_info = (21, 18, 25, 32, 52)

first_age, second_age, *rest_age, last_age = age_info

print(first_age)
print(second_age)
print(rest_age)
print(last_age)

    # example
def get_screensize():
    return 1920, 1080

    # unpacking
width, height = get_screensize()

print(width)
print(height)



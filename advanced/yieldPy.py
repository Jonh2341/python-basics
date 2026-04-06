# storing the whole text

# def fetch_lines(filename):
#     with open(filename, 'r') as file:
#         lines = []
#         for line in file:
#             lines.append(line)
#         return lines
    
# print(fetch_lines('forest.txt'))

# storing only specific line

def fetch_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line

res = fetch_lines('forest.txt')

print(res)

print(next(res))
print(next(res))
print(next(res))
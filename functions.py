users = {"Jack": 21, "Chiesa": 25, "Robert": 18, "Johnny": 42}

def average(list):
    list_values = list.values()
    sum_list_value = sum(list_values)
    list_lenght_value = len(list_values)

    res_value = sum_list_value / list_lenght_value
    print(f'average value for {list_values} is: {res_value}') 

average(users)

# lambda func

double_enhancer = lambda x: x * 2
print(double_enhancer(10)) 
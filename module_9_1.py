def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        result = function(int_list)
        results[function.__name__] = result
    return results

my_list = [1, 2, 3, 4, 5]

def sum_list(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        total += number
    return total

def multiply_list(list_of_numbers):
    product = 1
    for number in list_of_numbers:
        product *= number
    return product


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
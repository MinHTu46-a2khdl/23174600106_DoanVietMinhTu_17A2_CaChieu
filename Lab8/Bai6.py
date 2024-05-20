def filter_odd_numbers(lst):
    return list(filter(lambda x: x % 2 != 0, lst))

#b
def filter_even_numbers(lst):
    return list(filter(lambda x: x % 2 == 0, lst))
#c
def map_cubed_numbers(lst):
    return list(map(lambda x: x**3, lst))
#d
def map_and_filter_even_cubed_numbers(lst):
    even_numbers = filter(lambda x: x % 2 == 0, lst)
    return list(map(lambda x: x**3, even_numbers))
#e
def map_and_filter_odd_squared_numbers(lst):
    odd_numbers = filter(lambda x: x % 2 != 0, lst)
    return list(map(lambda x: x**2, odd_numbers))

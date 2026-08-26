import math

#Exercise 1 
#Question 1 
def add_two_numbers(num_one, num_two):
    return num_one + num_two 
print(add_two_numbers(9, 4))

#Question 2 
def area_circle(radius):
    return math.pi * (radius ** 2)
print(area_circle(5))

#Question 3
def add_all_nums(*nums):
    total = 0 
    for num in nums: 
        total += num
    return total
print(add_all_nums(3, 9, 6))

#Question 4 
def convert_temp(celsius):
    return celsius * (9/5) + 32
print(convert_temp(76))

#Question 5
def check_season(month):
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
print(check_season('February'))

#Question 6
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(3, 4 , 6, 8))

#Question 7
def quadratic(a, b, c):
    discriminant = (b ** 2) - 4 * a * c
    x_1 = ((-b) + math.sqrt(discriminant)) / (2 * a) 
    x_2 = ((-b) - math.sqrt(discriminant)) / (2 * a) 
    return x_1, x_2
print(quadratic(1, 5, 6))

#Question 8
fruits = ['Apple', 'Banana', 'Orange']

def print_list(items):
    for item in items:
        print(item)

print_list(fruits)

#Question 9 
def reverse_list(original):
    reversed_list = []  
    
    for item in original:
        reversed_list.insert(0, item)
        
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))

#Question 10
def capitalize_list_items(lower):
    capitalize_list = []
    
    for item in lower:
        capitalize_list.append(item.capitalize())
        
    return capitalize_list
print(capitalize_list_items(['apple', 'banana', 'pineapple']))

#Question 11
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']

def add_item(food, extra):
    food.append(extra)
    return food

print(add_item(food_stuff, 'Meat'))

#Question 12
def remove_item(food, less):
    food.remove(less)
    
    return food

print(remove_item(food_stuff, 'Mango'))

#Question 13
def sum_of_numbers(number):
    total = 0 
    for num in range(0, number + 1):
        total += num
        
    return total 

print(sum_of_numbers(5))

#Question 14
def sum_of_odds(n):
    total = 0 
    for num in range(0, n + 1):
        if num % 2 == 1:
            total += num
    
    return total 

print(sum_of_odds(10))

#Question 15
def sum_of_evens(x):
    total = 0
    for numb in range(0, x + 1):
        if numb % 2 == 0:
            total += numb
    return total

print(sum_of_evens(4))

#Exercise 2
#Question 1 
def evens_and_odds(numeral):
    
    even_count = 0
    odd_count = 0
    
    for num in range(0, numeral + 1):
        if num % 2 == 0:
            even_count += 1
        elif num % 2 == 1:
            odd_count += 1

    print(f'The number of evens are {even_count}')
    print(f'The number of odds are {odd_count}')

print(evens_and_odds(100))

#Question 2
def factorial(whole):
    result = 1
    
    for num in range(1, whole + 1):
        result *= num
    return result

print(factorial(5))

#Question 3 
def is_empty(emp):
    if not emp:
        return 'EMPTY'
    else: 
        return 'This is not empty.'

print(is_empty([]))
print(is_empty([1, 2, 3]))

#Question 4A
def calculate_mean(nums):
    total = 0 
    for number in nums:
        total += number  
        
    mean = total / len(nums)
    return mean 

print(calculate_mean([10, 20, 30, 40, 50]))

#4B
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    
    if length % 2 == 1:
        middle = length // 2 
        return sorted_numbers[middle]
    else: 
        middle_right = length // 2 
        middle_left = middle_right - 1 
        median = (sorted_numbers[middle_left] + sorted_numbers[middle_right]) / 2
    return median

print(calculate_median([10, 20, 30, 40, 50]))
print(calculate_median([10, 20, 30, 40]))

#4C
def calculate_mode(num):
    counts = {}
    
    for number in num:
        if number in counts:
            counts[number] += 1 
        else: 
            counts[number] = 1 

    max_count = max(counts.values())
    for number, count in counts.items():
        if count == max_count:
            return number

print(calculate_mode([2, 2, 2, 5, 5, 7]))

#4D
def calculate_range(numb):
    largest_num = max(numb)
    smallest_num = min(numb)
    
    number_range = largest_num - smallest_num
    return number_range

print(calculate_range([4, 8, 12, 20]))

#4E
def calculate_variance(number):
    mean = calculate_mean(number)

    squared_diff_total = 0
    for value in number:
        difference = value - mean 
        squared_diff_total += difference ** 2 
    
    variance = squared_diff_total / len(number)
    
    return variance

print(calculate_variance([10, 20, 30, 40, 50]))

#4F
def calculate_std(nums):
    variance = calculate_variance(nums)
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation

print(calculate_std([10, 20, 30, 40, 50]))

#Question 5 
def greet(name = 'Guest'):
    print(f'Hello, {name}!')
    
greet()
greet('Alice')

#Question 6
def show_args(**kwargs):
    result = 'Received: '
    for key, value in kwargs.items():
        result +=(f'{key}: {value}, ')
        
    result = result[:-2]
    print(result)

show_args(name="Alice", age=30, city="New York")

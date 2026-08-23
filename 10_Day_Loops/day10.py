#Exercise 1

#Question 1 
#while loop
number = 0
while number < 11:
    print(number)
    number += 1 

#For loop
for number in range(11):
    print(number)

#Question 2 
#While loop
count = 10
while count >= 0:
    print(count)
    count -= 1

#For loop
for count in range(10, -1, -1):
    print(count)

#Question 3 
for number1 in range(1, 8):
    print('#' * number1)

#Question 4
for row in range(8):
    for column in range(8):
        print('#', end= ' ')
    
    print()

#Question 5
for multiple in range(0,11):
    print(f'{multiple} x {multiple} = {multiple * multiple}')

#Question 6
programs = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for program in programs:
    print(program)

#Question 7 
even = 0
for even in range(0, 101, 2):
    print(even)

odd = 1 
for odd in range(1, 100, 2):
    print(odd)

#Exercise 2
#Question 1
total = 0
for num in range (0,101):
    total += num
print(f'The sum of all numbers is {total}')

#Question 2

even_sum = 0
odd_sum = 0

for numb in range (0,101):
    if numb % 2 == 0: 
        even_sum += numb
    else: 
        odd_sum += numb
print(f'The sum of all even numbers is {even_sum}')
print(f'The sum of all odd numbers is {odd_sum}')




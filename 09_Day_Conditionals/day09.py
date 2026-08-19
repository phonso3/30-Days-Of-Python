# Exercise 1
# Question 1 
age = int(input('Please enter your age: '))
years_left = 18 - age 

if age >= 18:
    print('You are old enough to drive')
else:
    print(f'You need {years_left} more years to learn to drive')

#Question 2 
my_age = 25
your_age = int(input('Your age: '))
age_diff = your_age - my_age
diff_age = my_age - your_age

if your_age > my_age:
    if age_diff == 1:
        print(f'You are {age_diff} year older than me.')
    else:
        print(f'You are {age_diff} years older than me.')
elif my_age > your_age:
    if diff_age == 1: 
        print(f'I am {diff_age} year older than you.')
    else: 
        print(f'You are {diff_age} years younger than me.')
else:
    print('We are the same age.')

#Question 3 
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

# Exercise 2 
# Question 1 
grade = int(input('Enter number grade(0-100): ' ))

if grade < 0 or grade > 100:
    print('Invalid Grade')
elif grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

#Question 2 
month = (input('Enter a month: '))
month = month.capitalize()

def get_season(month):
    if month in ['September', 'October', 'November']:
        print('Autumn')
    elif month in ['December', 'January', 'February']:
        print('Winter')
    elif month in ['March', 'April', 'May']:
        print('Spring')
    elif month in ['June', 'July', 'August']:
        print('Summer')
    else:
        print('Invalid month!')

get_season(month)

#Question 3
fruit = input('Enter a fruit: ')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = fruit.lower()

if fruit in fruits: 
    print('That fruit already exist in the list.')
else: 
    fruits.append(fruit)
    print(fruits)

# Exercise 3 
person = {
    'first_name':'Jackson',
    'last_name':'Taylor',
    'gender':'Male',
    'age':'23',
    'is_married':'True',
    'country':'USA',
    'skills':['JavaScript', 'Python', 'HTML'],
    'city':'Houston',
    'address':{
        'street':'Candyland Road',
        'zipcode':'21098'
    }
}

if 'skills' in person:
    print(person['skills'][1])
    
if 'Python' in person['skills']:
    print(person['skills'])
    
if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('He is a front end developer.')
elif 'Python' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer.')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
else:
    print('Unknown title.')
    
if person['is_married'] and person['country'] == 'USA':
    print(f"{person['first_name']} {person["last_name"]} lives in {person['country']}. He is married.")

#Exercise 1

#Question 1 
empty_list = []

#Question 2 
bball_players = ['Curry', 'James', 'Edwards', 'Durant', 'Jokic', 'Ball', 'Morant']

#Question 3 
print('Names of Players:', bball_players)
print('How many Players?', len(bball_players))

#Question 4
first_name = bball_players[0]
print(first_name)
middle_name = bball_players[3]
print(middle_name)
last_name = bball_players[6]
print(last_name)

#Question 5 
mixed_data_types = [
    'Alphonso',
    25,
    5.10,
    'Single',
    'Florida'
]

#Question 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Question 7
print(it_companies)

#Question 8 
print('Number of IT Companies:', len(it_companies))

#Number 9
first_comp = it_companies[0]
print(first_comp)
second_comp = it_companies[3]
print(second_comp)
third_comp = it_companies[6]
print(third_comp)

#Question 10
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[2] = 'NVIDIA'
print(it_companies)

#Question 11
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.append('NTT')
print(it_companies)

#Question 12
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.insert(3, 'Accenture')
print(it_companies)

#Question 13
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
upper_it = 'Amazon'
if upper_it in it_companies:
    it_companies[it_companies.index(upper_it)] = upper_it.upper()
print(it_companies)

#Question 14 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
seperator = ' #; '
seperator.join(it_companies)
print(seperator.join(it_companies))

#Question 15
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
one_it = 'Facebook'
if one_it in it_companies:
    print('This is an IT Company')
else:
    print('This is not an IT Company')

#Question 16
it_companies.sort()
print(it_companies)

#Question 17
it_companies.reverse()
print(it_companies)

#Question 18
first_three = it_companies[0:3]
print(first_three)

#Question 19
last_three = it_companies[-3:]
print(last_three)

#Question 20
middle = it_companies[3:4]
print(middle)

#Question 21
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(0)
print(it_companies)

#Question 22
it_companies.pop(2)
it_companies.pop(2)
print(it_companies)

#Question 23
it_companies.pop(-1)
print(it_companies)

#Question 24
it_companies.clear()
print(it_companies)

#Question 25
del it_companies

#Question 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
codes = front_end + back_end
print(codes)

#Question 27
full_stack = codes.copy()

redux_position = full_stack.index('Redux')

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')

print(full_stack)











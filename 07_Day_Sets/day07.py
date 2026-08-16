# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercise 1 
#Question 1 
print(len(it_companies))

#Question 2 
it_companies.add('Twitter')
print(it_companies)

#Question 3
it_companies.update(['Accenture', 'NVIDIA', 'Alphabet'])
print(it_companies)

#Question 4
it_companies.remove('NVIDIA')
print(it_companies)

#Question 5
print('remove method will raise errors, discard method does not! ')

#Exercise 2
#Question 1
print(A.union(B))

#Question 2 
print(A.intersection(B))

#Question 3 
print(A.issubset(B))

#Question 4 
print(A.isdisjoint(B))

#Question 5 
print(A.union(B))
print (B.union(A))

#Question 6 
print(A.symmetric_difference(B))

#Question 7
del A
del B

#Exercise 3
#Question 1
print(len(age))

age = set(age)
print(age)

print(len(age))

print('The list is bigger than the set.')

#Question 2 
print('Strings: You cannot change, add, or remove characters from an existing string. Any alteration creates a brand-new string')
print ('List: Fully changeable. You can add, remove, or modify items whenever you want.')
print('Sets: utomatically eliminates duplicates. If you add 2 twice, it only saves it once.')
print('Tuples: Cannot be changed after creation. You cannot add, remove, or alter items. This makes them faster than lists and safe for constant data.')

#Question 3 
sentence = 'I am a teacher and I love to inspire and teach people.'

words = sentence.replace('.','').split()

unique_words = set(words)

print(len(unique_words))




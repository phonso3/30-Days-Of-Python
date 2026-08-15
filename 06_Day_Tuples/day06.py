#Question 1 
empty_tuple = ()
print(empty_tuple)

#Question 2
bro = ('Jack', 'Kenny', 'Tyson')
sis = ('Taylor', 'Maggie', 'Becca')

print(bro)
print(sis)

#Question 3 
siblings = bro + sis 
print(siblings)

#Question 4 
print(len(siblings))

#Question 5 
parents = ('Jeffrey', 'Pamela')
family_members = parents + siblings 
print(family_members)

#Excercise 2
#Question 1
father, mother, *siblings = family_members 
print(family_members)

#Question 2
fruits = ('Apple', 'Orange', 'Peach', 'Strawberry')
vegetables = ('Broccoli', 'Carrot', 'Cauliflower', 'Mushroom')
animal_products = ('Beef', 'Eggs', 'Milk', 'Chicken')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#Question 3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#Question 4 
middle_items = food_stuff_lt[5:7]
print(middle_items)

#Question 5
first_items = food_stuff_lt[0:3]
last_items = food_stuff_lt[-3:]
print(first_items + last_items)

#Quesion 6 
del food_stuff_tp

#Question 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print ('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
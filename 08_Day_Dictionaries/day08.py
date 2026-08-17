#Question 1
dog = {}

#Question 2 
dog = {
    'Color':'Brown',
    'Breed':'Golden Retriever',
    'Legs':'Four',
    'Age':'3'
}

print(dog)

#Question 3
student = {
    'first_name':'Jackson',
    'last_name':'Taylor',
    'gender':'Male',
    'age':'23',
    'is_married':'Single',
    'country':'USA',
    'skills':['JavaScript', 'Python', 'HTML'],
    'city':'Houston',
    'address':{
        'street':'Candyland Road',
        'zipcode':'21098'
    }
}
print(student)

#Question 4
print(len(student))

#Question 5 
print(student['skills'])

#Question 6
student['skills'].append('HTML')
student['skills'].append('C')

print(student)

#Question 7
stu_keys = student.keys()
print(stu_keys)

#Question 8
stu_values = student.values()
print(stu_values)

#Question 9
print(student.items())

#Question 10
del student['is_married']
print(student)

#Question 11 
del dog


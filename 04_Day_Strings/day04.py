#Number 1 
space =  ' ' 
question_one = 'Thirty'
question_onea = 'Days'
question_oneb = 'Of'
question_onec = 'Python'
full_answer = question_one + space + question_onea + space + question_oneb + space + question_onec

#Number 2
question_two = 'Coding'
question_twoa = 'For'
question_twob = 'All'
full_answer_two = question_two + space + question_twoa + space + question_twob

#Number3, 4, 5 
company = 'Coding For All'
print(company)
print(len(company))

#Number 6
print(company.upper())

#Number 7 
print(company.lower())

#Number 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Number 9
slice = company[6:12]
print(slice)

#Number 10
print(company.find('Coding'))

#Number 11
print(company.replace('Coding', 'Python'))

#Number 12
everyone = 'Python for Everyone'
print(everyone.replace('Everyone', 'All'))

#Number 13
print(company.split(space))

#Number 14
social_media = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(social_media.split(','))

#Number 15
print(company[0])

#Number 16
print(len(company) - 1)

#Number 17
print(company[10])

#Number 18
#everyone = 'Python for Everyone'
pfe = everyone.split()
print(pfe[0][0] + pfe[1][0] + pfe[2][0])

#Number 19
cfa = company.split()
print(cfa[0][0] + cfa[1][0] + cfa[2][0])

#Number 20 
print(company.index('C'))

#Number 21 
print(company.index('F'))

#Number 22
people = 'Coding for All People'
print(people.rfind('l'))

#Number 23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

#Number 24
print(sentence.rindex('because'))

#Number 25
start = sentence.index('because')
end = sentence.rindex('because') + len('because')

cut_sentence = sentence[31:54]
print(cut_sentence)

#Number 26
print(sentence.find('because'))

#Number 27 
start = sentence.index('because')
end = sentence.rindex('because') + len('because')

phrase = sentence[31:54]
print(phrase)

#Number 28
print(company.startswith('Coding'))

#Number 29
print(company.endswith('coding'))

#Number 30
extend_company = '   Coding For All     ' 
print(extend_company.strip())

#Number 31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

#Number 32
libraries = 'Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'
seperator = ' # '
print(seperator.join(libraries))

#Number 33
number_33 = 'I am enjoying this challenge. \nI just wonder what is next.'
print(number_33)

#Number 34
table = 'Name\tAge\tCountry\tCity\nAlphonso\t25\tUSA\tHawthorne'
print(table)

#Number 35
pi = 3.14
radius = 10
area = pi * radius ** 2

print(f'The area of a circle with radius {radius} is {area} meters square.')

#Number 36
a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

age = 25 
my_height = 5.10

print('Age:', age)
print('Height:', my_height)

z = 10 + 5j
print('Complex number:', z)

base = float(input('Enter the base:'))
height = float (input('Enter the height:'))
area = 0.5 * base * height

print('Area of triangle:' , area)

#Perimeter
side_a = float (input('Enter side a:'))
side_b = float (input('Enter side b:'))
side_c = float (input('Enter side c:'))
perimeter = side_a + side_b + side_c

print('Perimeter of triangle:' , perimeter)


#Rectangle
length = float (input('Enter the length:'))
width = float (input('Enter the width:'))
area_rectangle = length * width 

print('Area of rectangle:' , area_rectangle)

perimeter_rectangle = 2 * (length + width)
print('Perimeter of rectangle:' , perimeter_rectangle)

#Circle
pi = 3.14
radius = float (input('Enter the radius:'))
area_circle = pi * radius ** 2 

print('Area of circle:' , area_circle)

circumference = 2 * pi * radius 
print('Circumference of circle:' , circumference)

#Slope
#y = 2x - 2
slope = 2
print('Slope of the line y = 2x - 2:' , slope)
x_intercept = 2 / slope 
print('X-intercept of the line y = 2x - 2:' , x_intercept)
y_intercept = 2 * 0 - 2 
print('Y-intercept of the line y = 2x - 2:' , y_intercept)

new_slope = (10 - 2) / (6 - 2)
print('Slope of the line:' , new_slope)
distance = ((6 - 2) ** 2 + (10 - 2) ** 2) ** 0.5
print('The Euclidean distance is:' , distance)

print(slope == new_slope)

#Formula 
x = -3
y = x ** 2 + 6 * x + 9
print('The value of y:' , y)

#ON
print(len('python') > len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon')

print ('on' not in 'python' and 'on' not in 'dragon')


print(float(len('python')))
str(float(len('python')))
print(str(float(len('python'))))

value = str(float(len('python')))
print(value)
print(type(value))

#Math 
number = input('Enter even number:')
print(int(number) % 2 == 0)

floor_div = 7 // 3 == int(2.7)
print(floor_div)

type('10') == type(10)
print(type('10') == type(10))

int(float('9.8')) == 10
print(int(float('9.8')) == 10)

work_hours = int(input('Enter hours worked:'))
hourly_rate = float(input('Hourly rate:'))
weekly_earning = work_hours * hourly_rate 
print('$', weekly_earning)

years_lived = int(input('Number of years lived:'))
seconds_lived = years_lived * 365 * 24 * 60 ** 2 
print('You have lived for', seconds_lived, 'seconds.')

num_one = 1
num_two = 2
num_three = 3
num_four = 4
num_five = 5

print(num_one, num_one ** 0, num_one ** 1, num_one ** 2, num_one ** 3)
print(num_two, num_two ** 0, num_two ** 1, num_two ** 2, num_two ** 3)
print(num_three, num_three ** 0, num_three ** 1 , num_three ** 2, num_three ** 3)
print(num_four, num_four ** 0, num_four ** 1, num_four ** 2, num_four ** 3)
print(num_five, num_five ** 0, num_five ** 1, num_five ** 2, num_five ** 3)  






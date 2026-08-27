#Exercise 1 
import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''
    for _ in range(6):
        random_character = random.choice(characters)
        user_id += random_character
    return user_id

print(random_user_id())

def user_id_gen_by_user():
    num_characters = int(input('Enter the number of characters: '))
    num_ids = int(input('Enter the numbers of IDs: '))
    
    characters = string.ascii_letters + string.digits
    
    for _ in range(num_ids):
        user_id = ''
        for _ in range(num_characters):
            random_char = random.choice(characters)
            user_id += random_char
        print(user_id)

user_id_gen_by_user()

def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (f'rgb({red}, {green}, {blue})')

print(rgb_color_gen())

#Exercise 2 
def list_of_hexa_colors(amount):
    colors = []
    hex_char = '0123456789abcdef'
    
    for _ in range(amount):
        hex_color = '#'
        
        for _ in range(6):
            random_hex = random.choice(hex_char)
            hex_color += random_hex
        
        colors.append(hex_color)
    
    return colors

print(list_of_hexa_colors(3))

def list_of_rgb_colors(amount):
    colors = []
    
    for _ in range(amount):
        rgb_color = rgb_color_gen()
        colors.append(rgb_color)
    
    return colors

print(list_of_rgb_colors(4))

def generate_colors(color_type, amount):
    if color_type == 'hexa':
        return list_of_hexa_colors(amount)
    elif color_type == 'rgb':
        return list_of_rgb_colors(amount)

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))

#Exercise 3
def shuffle_list(items):
    random.shuffle(items)
    return items

print(shuffle_list([10, 5, 76, 22, 8]))

def unique_random_numbers():
    numbers = []
    
    while len(numbers) < 7:
        random_num = random.randint(0, 9)
        
        if random_num not in numbers:
            numbers.append(random_num)
    
    return numbers

print(unique_random_numbers())
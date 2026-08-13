#Exercise 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

min_age = 19
max_age = 26

ages.append(min_age)
ages.append(max_age)

ages.sort()
len(ages)
middle = len(ages) // 2 
median = (ages[middle - 1] + ages[middle]) / 2
print(median)

average_age = sum(ages) / len(ages)
print(average_age)

age_range = max_age - min_age
print(age_range)

min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print(min_diff)
print(max_diff)


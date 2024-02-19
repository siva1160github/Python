#bool, int, string -> won't affect original copy

name = 'siva'

other_name = name
other_name = 'krishna'

age = 28
other_age = age

other_age = 26
print(name, other_name)

print(age, other_age)

#list, set, dict -> always hold a reference

fruits = ['apple', 'banana', 'kiwi']
other_fruit = fruits.copy()

other_fruit.append('Dragon fruit')

print(fruits, other_fruit)
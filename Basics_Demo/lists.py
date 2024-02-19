users = ['abc', 'xxx', 'yyy', 'zzz']

users.append('wwww')
users.insert(0,'first Item')

users.pop()
print(users)

print(users[2:])

# Repeat
numbers = [1, 2] * 5
print(numbers)

# Unpacking
items = ['laptop', 'mobile', 'tablet']
laptop, *others = items
print(laptop)
print(others)

# Tuples
letters = ('a', 'b', 'c', 123)
print(letters[2])

# Sets
sets = {'a', 'b', 'a','c', 'd', 123}
sets.remove("c")
print(sets)
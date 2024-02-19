def greeting(name):
    print(f'Hello {name}. Good Morning!')

name = input('Enter your name: ')
greeting(name)

def multiply(num1 = 10, num2 =2):
    return num1 * num2

output = multiply(15)
print(output)

output = multiply(num1=24, num2=24)
print(output)

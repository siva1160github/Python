#Falsy values

0
""
[]

isLoggedIn = True

if isLoggedIn:
    print("You are logged in")

name = input("Enter your name ")
age = int(input("Enter your age "))

if name.upper() == 'SIVA' and age > 25:
    print("You are eligible Siva")
elif name.upper() == 'KRISHNA' and age > 25:
    print("You are eligible Krishna")
else:
    print(f"Sorry,{name} is not eligible")
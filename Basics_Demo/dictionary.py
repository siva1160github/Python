user = {
    "name" : 'siva',
    "age" : 28,
    "profession" : "Software Developer",
    "Skills" : ["C#", "Javascript", "Azure"]
}

user["profession"] = "FSD"

for key, value in user.items():
    print(key, value)


if "name" in user:
    print("key is available")
else:
    print("key doesn't exist")

#it will return a tuple
for item in user.items():
    print(item)
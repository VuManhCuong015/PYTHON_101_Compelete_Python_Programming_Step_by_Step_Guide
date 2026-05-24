#ex1
person = {"name": "Joseph", "age": 25, "city": "London"}

person["email"] = "joseph@gmail.com"
person["age"] = 28
del person["city"]
print(person)

#ex2
person = {"name": "Joseph", "age": 25, "city": "London"}

for key, value in person.items():
    print(key, ":", value)

#ex3
person = {"name": "David", "age": 30, "city": "Paris"}

print(person.keys())
print(person.values())
print(person.get("name"))
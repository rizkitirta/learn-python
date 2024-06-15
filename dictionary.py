user =  {
    "name": "Rizki Tirta",
    "age": 22,
    "is_married": False,
}
print(user)
print("===============")

# get value from dictionary
print(user["name"])
print(user["age"])
print("===============")

# add new key value to dictionary
user["address"] = "Jakarta"
print(user)
print("===============")

# remove key value from dictionary
user.pop('age')
print(user)
print("===============")

# check if key exist in dictionary
print("name" in user)
print("username" in user)
print("===============")

# get value from dictionary with get method
username = user.get("username","anonymous") # if key not exist return anonymous (default value)
print(username)
print("===============")

# loop through dictionary
for key in user:
    print(f"{key.title()}: {user[key]}")
    print("===============")

print("===============")

# loop through dictionary with items method
for key, value in user.items():
    print(f"{key.title()}: {value}")
    print("===============")

print("===============")


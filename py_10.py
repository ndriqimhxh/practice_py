# Tuples  - type of list that cannot be accessed or changed
numbers = (1, 2, 3)
# numbers.index()  used only to get information from tuples

# Unpacking
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x, y, z = coordinates   #assign to other variables the values inside a list
print(x,y,z)

#Dictionaries
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True           #like a template and each element of it cannot be duplicated
}
print(customer["name"])
print(customer.get("birthdate"))   #gives as a response None boolean and not an error
customer["age"] = 40             #update the dictonary

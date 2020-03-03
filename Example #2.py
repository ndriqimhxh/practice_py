a = int(input("Number of elements of the list: "))
numbers = []
i = 1
for number in range(a):
    number = int(input(f"{i} number: "))
    i += 1
    numbers.append(number)
print(numbers)
numbers.sort()
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

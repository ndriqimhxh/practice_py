#Print all numbers in range divisible by a given number
var = True
while var:
    try:
        a = int(input("Range: "))
        b = int(input("Number: "))
        var = False
    except ValueError:
        print("Enter an integer!")

for num in range(a):
    mod = num % b
    if mod == 0:
        print(num)


#Accept 3 digits and print all possible combinations of them
var = True
while var:
    try:
        x = int(input("1st number: "))
        y = int(input("2nd number: "))
        z = int(input("3rd number: "))
        var = False
    except ValueError:
        print("Enter an integer!")

numbers = []
numbers.append(x)
numbers.append(y)
numbers.append(z)

for i in range(3):
    for j in range(3):
        for k in range(3):
            print(numbers[i], numbers[j], numbers[k])


#Accept an integer and sum all the numbers up to that one
var = True
while var:
    try:
        x = int(input(">"))
        var =  False
    except ValueError:
        print("Enter an integer!")

sum = 0
for num in range(x):
    sum += num
sum += x
print(f"Total sum: {sum}")

class List:
    def __init__(self):
        self.list = []
    def __add__(self, other):
        return self.list.append(other)
    def display(self):
        for element in self.list:
            print(element)
    def delete(self):
        return self.list.clear()
    def remove(self, other):
        return self.list.remove(other)

numbers1 = [1, 3, 4, 5]
numbers = List()
numbers.display()
numbers.__add__(3)
numbers.display()

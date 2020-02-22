#2D Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

#List methods
numbers = [5, 2, 1, 7, 4, 20]
numbers.sort()
numbers2 = numbers.copy()         #copy lists
numbers.insert(0, 3)      #add a number at a speacial place in the list
numbers.remove(5)
print(numbers)
numbers.clear()    #clear remove all numbers
numbers.index(2)          #place of the number 5 in the list
print(numbers.index(2))   #gives an error if the number is not in the list
print(20 in numbers)      #it doesnt give an error if the number is not in the list
numbers.clear()    #clear remove all numbers

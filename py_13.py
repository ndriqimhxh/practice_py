def emoji_creater(message):
    words = message.split(" ")
    output = ""
    for word in words:
        output += word
    return output


message = input(">")
print(emoji_creater(message))

#Exceptions
#Errors - try except - used to not crash the program
try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("You should answer an integer!")

#example
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:               #different kinds of exception
    print("Enter an integer!")
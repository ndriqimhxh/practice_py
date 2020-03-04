#Functions
def greet_user():             #defining a function
    print("Hi, there")
                            #2 lines of break after each class or function definition

print("Start")
greet_user()
print("Finish")

def greet_user1(first_name, last_name):       #function with argument
    print(f'Hi {first_name} {last_name}!')


greet_user1("Ndriqim", "Hoxha")

#Example
def square(number):
    return number * number


result = square(2)
print(result)
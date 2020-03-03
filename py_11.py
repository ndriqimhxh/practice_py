phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
for ch in phone:
    output = digits_mapping.get(ch, "!") + " "   #get function, it will put ! if it doesnt find the element in the dictionary
    print(output)

message = input(">")
words = message.split(' ')       #whereever it sees a space it will split the word
print(words)


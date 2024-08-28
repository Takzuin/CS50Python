name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()
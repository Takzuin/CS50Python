name = input("What's your name? ")

file = open(".idea/names.txt", "a")
file.write(name)
file.close()
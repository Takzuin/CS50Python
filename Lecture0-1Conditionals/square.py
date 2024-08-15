def main():
    x = int(input("What's x?"))
    print("z squared is", square(x))

#(Square)Traduccion: Al cuadrado
def square(n):
    return pow(n, 2)

main()
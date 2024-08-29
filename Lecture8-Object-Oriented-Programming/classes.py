### Classes ###


#En el init se define el constructor, objeto y se le da sus propiedades
class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} Esta caminando")

my_person = Person("Bruce", "Wayne")
print(my_person.full_name)
my_person.walk()
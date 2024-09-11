import os

class Animal:
    breed = ''
    price = 0
    def __init__(self,breed, price):
        self.breed = breed
        self.price = price
    def Move():
        raise("Who am I?")

class Fish(Animal):
    def Move():
        print("Blob blob")

class Bird(Animal):
    def Move():
        print("Shphpfpfpfpf")

class ZooShop:
    animals = list()

    def __init__(self, animals):
        self.animals = animals

    def TheMoastCheresRechkyUnCheapBreed(self):
        richestBreed = ''
        richestPrice = -1
        for animal in self.animals:
            if animal.price > richestPrice and animal.breed != richestBreed:
                richestBreed = animal.breed
                richestPrice = animal.price

    def WriteFile(self):
        try:
            f = open("Animals.txt",'x')
        except:
            os.remove("Animals.txt")
            f = open("Animals.txt", 'x')

        for animal in self.animals:
            f.write("Breed: " + animal.breed + " Price: " + str(animal.price) + '\n')

ZooShop = ZooShop([Fish('Goldy', 52), Fish('Okun', 25), Fish('Shark', 2552)])

ZooShop.WriteFile()




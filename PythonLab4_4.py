class Gun:
    mass = 0
    price = 0
    damage = 0

    maxAmmo = 0
    currentAmmo = 0

    name = ""

    def __init__(self, mass, price, maxAmmo, name):
        self.mass = mass
        self.price = price
        self.name = name
        self.maxAmmo = maxAmmo
        self.currentAmmo = maxAmmo

    def Shoot():
        print("...")

    @staticmethod
    def Look():
        print("...")


class BFG9000(Gun):
    argonianSouls = 0

    def __init__(self, mass, price, maxAmmo, name, argonianSouls):
        super.__init__(mass, price, maxAmmo, name)
        self.argonianSouls = argonianSouls

    def _Shoot(self):
        if self.currentAmmo > 0:
            self.currentAmmo -= 1
            print("BOOOOOOOOOOOOOOOOOOOM")

    def Reload(self):
        self.currentAmmo = self.maxAmmo
        print("Click, plam, pshhhhhhh")

    @staticmethod
    def Look():
        print("HERE'S POWER!!")

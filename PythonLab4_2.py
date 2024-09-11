class Country:
    capital = ''
    square = 0
    peopleCount = 0
    def __init__(self,capital,square,peopleCount):
        self.capital = capital
        self.square = square
        self.peopleCount = peopleCount


def searchBySquare(countries, square):
    for country in countries:
        if country.square == square:
            print(country.capital)
            

def searchByPeopleCount(countries, peopleCount):
    for country in countries:
        if country.peopleCount == peopleCount:
            print(country.capital)

countries = [Country("Minsk", 522, 522),Country("Doneck", 52, 52),Country("Vilna", 52, 52),Country("Kiev", 52, 52),Country("Baghdad", 52, 52)]

searchBySquare(countries,522)
searchByPeopleCount(countries,522)
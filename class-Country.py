class Country(object):
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __str__(self):
        return self.name + " has a population of " + str(self.population) + " and is " + str(self.area) + " square km."

    def is_larger(self, other):
        if self.area > other.area:
            return True
        else:
            return False

    def population_density(self):
        return self.population/self.area

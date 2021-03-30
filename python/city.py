'''
Author: kvaden
10 April 2020
v1.0
'''


class City:
    def __init__(self, name=None, population=None, color=None, cubes=None,
                 research=False, connected_cities=None, players=None, owner=None):
        self.name = name
        self.population = population
        self.color = color
        self.cubes = cubes
        self.research = research
        self.connected_cities = connected_cities
        self.players = players
        self.owner = owner

    def __str__(self):
        return '{} is a {} city. Current diseases: {}. Current players: {} Research station: {}.\n'\
            .format(self.name, self.color, self.cubes, self.players, self.research)

    def __iter__(self):
        return self

    def infect(self, disease_color, intensity=1):
    # Increases the cubes of a given disease on a city.
        if self.cubes is None:
            self.cubes = {}
        for i in range(0, intensity):
            if disease_color in self.cubes:
                self.cubes[disease_color] += 1
            else:
                self.cubes[disease_color] = 1
        print(self.name, 'was infected with', disease_color)
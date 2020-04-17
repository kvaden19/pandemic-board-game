'''
Author: kvaden
15 April 2020
v1.0
'''

import matplotlib.pyplot as plt

class Map:
    def __init__(self, city_dict=None, routes=None, cities=None, players=None):
        self.city_dict = city_dict
        self.routes = routes
        self.cities = cities
        self.players = players

    def draw(self):
        # Set up the Axes object
        fig, ax = plt.subplots()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.set_xlim(0,20)
        ax.set_ylim(0,10)

        # Unpack the city locations and their labels
        city_x = []
        city_y = []
        labels = []
        for label, coordinates in self.city_dict.items():
            labels.append(label)
            city_x.append(coordinates[0])
            city_y.append(coordinates[1])

        # Set up the routes between cities
        route_x = []
        route_y = []
        for label in self.routes:
            route_x.append(self.city_dict[label][0])
            route_y.append(self.city_dict[label][1])

        # Create the plot
        plt.scatter(city_x, city_y, c='blue')
        plt.plot(route_x, route_y)
        for i, label in enumerate(labels):
            ax.annotate(label, (city_x[i], city_y[i]))

        for player in self.players:
            ax.annotate(player.name, (self.city_dict[player.location][0], self.city_dict[player.location][1]))

        for city in self.cities:
            if 'blue' in city.cubes:
                ax.annotate(city.cubes['blue'], (self.city_dict[city.name][0], self.city_dict[city.name][1]))
            if 'red' in city.cubes:
                ax.annotate(city.cubes['red'], (self.city_dict[city.name][0], self.city_dict[city.name][1]))
            if 'yellow' in city.cubes:
                ax.annotate(city.cubes['yellow'], (self.city_dict[city.name][0], self.city_dict[city.name][1]))
            if 'black' in city.cubes:
                ax.annotate(city.cubes['black'], (self.city_dict[city.name][0], self.city_dict[city.name][1]))

        plt.show()
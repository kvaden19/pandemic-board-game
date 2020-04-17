'''
Author: kvaden
10 April 2020
v1.0
'''


class Player:
    def __init__(self, name='Player1', role=None, hand=None, location=None, actions=4, cards_to_cure=5,
                 quarantine=False, event=None):
        self.name = name
        self.role = role
        self.hand = hand
        self.location = location
        self.actions = actions
        # self.cards_to_cure = cards_to_cure
        # self.quarantine = quarantine
        # self.event = event

    def __str__(self):
        return 'The {} is in {}. {} actions remain this turn.\n'.format(self.role, self.location.name, self.actions)

    def drive(self, city):
    # Uses one action to move to a connected city from the player's location
        self.location.players.remove(self.name)
        self.location = city
        self.location.players.append(self.name)
        self.actions -= 1
        print('DRIVE:', self.name, 'to', self.location.name)

    def direct(self, city):
    # Uses one action and a given city card to move to that city
        self.location.players.remove(self.name)
        self.location = city
        self.location.players.append(self.name)
        self.hand.remove(self.location)
        discard = self.location
        self.actions -= 1
        print('DIRECT:', self.name, 'to', self.location.name)
        return discard

    def charter(self, city):
    # Uses one action and the city card matching current location to move to any city
        discard = self.location
        self.location.players.remove(self.name)
        self.hand.remove(self.location)
        self.location = city
        self.location.players.append(self.name)
        self.actions -= 1
        print('CHARTER:', self.name, 'to', self.location.name)
        return discard

    def shuttle(self, city):
    # Uses one action to move from one city with a research station to another
    # Without error checking this looks exactly like drive
        self.drive(city)
        print('SHUTTLE:', self.name, 'to', self.location.name)

    def build(self):
    # Uses one action and the city card matching current location to build a research station
        discard = self.location
        self.hand.remove(self.location)
        self.location.research = True
        self.actions -= 1
        print('BUILD: Research station now in', self.location.name)
        return discard

    def treat(self, color):
    # Uses one action to remove a disease cube of a given color from the player's location
        self.location.cubes[color] -= 1
        self.actions -= 1
        print('TREAT: Removing one', color, 'cube from', self.location.name)

    def share(self, player, mode='receive'):
    # Uses one action to share card matching both players' location
        if mode == 'receive':
            self.hand.append(self.location)
            player.hand.remove(self.location)
            self.actions -= 1
            print('SHARE:', self.name, 'receives', self.location.name)
        elif mode == 'give':
            player.hand.append(self.location)
            self.hand.remove(self.location)
            self.actions -= 1
            print('SHARE:', self.name, 'gives', player.name, self.location.name)

    def cure(self, color, cards):
    # Uses one action and five cities of a color to cure the disease of that color
        for card in cards:
            self.hand.remove(card)
        color.cured = True
        self.actions -= 1
        print('CURE: The', color.color, 'disease is now cured.')
        return cards

    #def play_event(self)

    #Roles will be subclasses of Player


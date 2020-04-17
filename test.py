'''
Author: kvaden
10 April 2020
v1.0
This script tests the methods on Player, City, and Disease and makes sure the interactions between objects and
attributes are as expected.
'''

# old setup - needs refactored
# import classes
#
# # Set up some cities
# dc = classes.City(name='DC')
# atlanta = classes.City(name='Atlanta', research=True)
# chicago = classes.City(name='Chicago')
# miami = classes.City(name='Miami')
# toronto = classes.City(name='Toronto')
# berlin = classes.City(name='Berlin')
# karachi = classes.City(name='Karachi', research=True)
#
# # Set up players and hands
# player_discard = []
# kelly = classes.Player(name='Kelly', role='Medic', actions=4, location=chicago)
# chicago.players = [kelly.name]
# chicago.cubes['blue'] = 3
# emily = classes.Player(name='Emily', role='Scientist', actions=4, location=chicago)
#
# card_set = [dc, atlanta, miami, toronto, chicago]
# for city in card_set:
#     kelly.hand.append(city)
# emily.hand = [berlin]
#
# # Set up a disease
# red = classes.Disease()

import map, player, city

#Test drawing of map - PASS
'''
test_dict = {
    'SFN' : (2,8),
    'CHI' : (5,9),
    'ATL' : (6,6),
    'MTL' : (7,9),
    'WDC' : (8,6),
    'NYC' : (9,9)
    }

routes = ['SFN', 'CHI', 'ATL', 'WDC', 'NYC', 'MTL', 'CHI', 'MTL', 'WDC']

kelly = player.Player(name='Kelly', location='CHI')
players = [kelly]

montreal = city.City(name='MTL')
montreal.infect('blue')
dc = city.City(name='WDC')

montreal.players = [kelly.name]
dc.infect('blue')
dc.infect('red', intensity=2)
cities = [montreal, dc]

map = map.Map(city_dict=test_dict, routes=routes, cities=cities, players=players)
map.draw()
'''

#Test drive method - RETEST
'''
print('Testing DRIVE method. Player should update location and lose one action. Cities should update players.')
print(kelly, atlanta, dc)
kelly.drive(dc)
print(kelly, atlanta, dc)
'''

#Test charter method - RETEST
'''
print('Testing CHARTER method. Card matching current location should move from player hand to discard. Player should '
      'update location and lose one action. Cities should update players.')
print(kelly, atlanta, berlin)
print('Discard: ', end='')
for item in player_discard:
    print(item.name, end=' ')
print('\n')
print('Hand: ', end='')
for item in kelly.hand:
    print(item.name, end=' ')
print('\n')

player_discard.append(kelly.charter(berlin))

print(kelly, atlanta, berlin)
print('Discard: ', end='')
for item in player_discard:
    print(item.name, end=' ')
print('\n')
print('Hand: ', end='')
for item in kelly.hand:
    print(item.name, end=' ')
print('\n')
'''

#Test direct method - RETEST
'''
print('Testing DIRECT method. Card matching destination should move from player hand to discard. Player should update '
      'location and lose one action. Cities should update players.')
print(kelly, atlanta, toronto)
print('Discard: ', end='')
for item in player_discard:
    print(item.name, end=' ')
print('\n')
print('Hand: ', end='')
for item in kelly.hand:
    print(item.name, end=' ')
print('\n')

player_discard.append(kelly.direct(toronto))

print(kelly, atlanta, toronto)
print('Discard: ', end='')
for item in player_discard:
    print(item.name, end=' ')
print('\n')
print('Hand: ', end='')
for item in kelly.hand:
    print(item.name, end=' ')
print('\n')
'''

#Test shuttle method - RETEST
'''
print('Testing SHUTTLE method. Player should update location to another city with a research station and lose one '
      'action. Cities should update players.')
print(kelly, atlanta, karachi)
kelly.shuttle(karachi)
print(kelly, atlanta, karachi)
'''

#Test build method - RETEST
'''
print('Testing BUILD method. Card matching current location should move from player hand to discard. Player should '
      'lose one action. Current location research station should flip to TRUE.')
print(kelly, chicago)
print('Discard: ', end='')
for item in player_discard:
    print(item.name, end=' ')
print('\n')
print('Hand: ', end='')
for item in kelly.hand:
    print(item.name, end=' ')
print('\n')

player_discard.append(kelly.build())

print(kelly, chicago)
print('Discard: ', end='')
for item in player_discard:
    print(item.name, end=' ')
print('\n')
print('Hand: ', end='')
for item in kelly.hand:
    print(item.name, end=' ')
print('\n')
'''

#Test treat method - RETEST
'''
print('Testing TREAT method. Player should lose one action. Current city cube count should decrease by one.')
print(kelly, chicago)
kelly.treat('blue')
print(kelly, chicago)
'''

#Test share method in give mode - RETEST
'''
print('Testing SHARE method in GIVE mode. Card matching current location should move from player one hand to player '
      'two hand. Player should lose one action.')
print(kelly, '\n', 'Kelly Hand: ', end='')
for item in kelly.hand:
    print(item.name, end=' ')
print('\n')
print(emily, '\n', 'Emily Hand: ', end='')
for item in emily.hand:
    print(item.name, end=' ')
print('\n')

kelly.share(emily, mode='give')

print(kelly, '\n', 'Kelly Hand: ', end='')
for item in kelly.hand:
    print(item.name, end=' ')
print('\n')
print(emily, '\n', 'Emily Hand: ', end='')
for item in emily.hand:
    print(item.name, end=' ')
print('\n')
'''

#Test share method in receive mode - RETEST
'''
print('Testing SHARE method in RECEIVE mode. Card matching current location should move from player two hand to player '
      'one hand. Player should lose one action.')
print(kelly, '\n', 'Kelly Hand: ', end='')
for item in kelly.hand:
    print(item.name, end=' ')
print('\n')
print(emily, '\n', 'Emily Hand: ', end='')
for item in emily.hand:
    print(item.name, end=' ')
print('\n')

kelly.share(emily, mode='receive')

print(kelly, '\n', 'Kelly Hand: ', end='')
for item in kelly.hand:
    print(item.name, end=' ')
print('\n')
print(emily, '\n', 'Emily Hand: ', end='')
for item in emily.hand:
    print(item.name, end=' ')
print('\n')
'''

#Test cure method - RETEST
'''
print('Testing CURE method. Player should lose one action. Five cards should move from players hand to discard pile. '
      'Disease should flip to cured.')
print(kelly, red)
print('Discard: ', end='')
for item in player_discard:
    print(item.name, end=' ')
print('\n')
print('Hand: ', end='')
for item in kelly.hand:
    print(item.name, end=' ')
print('\n')

player_discard.extend(kelly.cure(red, card_set))

print(kelly, red)
print('Discard: ', end='')
for item in player_discard:
    print(item.name, end=' ')
print('\n')
print('Hand: ', end='')
for item in kelly.hand:
    print(item.name, end=' ')
print('\n')
'''

#Test infect method - RETEST
'''
print('Testing INFECT method. Disease count of a given color should increase by 1.')
print(atlanta)
atlanta.infect(red.color)
print(atlanta)
'''



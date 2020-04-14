'''
Here's where I would write a script for playing, either with computer players or human ones
Vanilla Pandemic only for now

Decks can be lists - only funcs needed are .pop and random.shuffle

Phase 1: Text based game that 2 or more humans can pass + play.
    - Put this on GitHub
    - Write MVP gameplay script - no Events, Roles, and no one is trying to break it
        - Need some kind of GUI
        - Write the setup
        - Write the gameplay
    - Build 7 Player subclasses
    - Build 5 Event subclasses
    - Add error checking
Phase 2: Deploy an console-based Python app over the web and have it collect data
    - Build a data pipeline
    - Play / share / accumulate data
Phase 3: Build a ML-based automated player

'''

#Setup
'''
player_deck = []
player_discard = []
infection_deck = []
infection_discard = []

outbreaks = 0
infection_rate = 0

'''

#Gameplay
#Treehouse -> Databases in Python -> Diary App -> Switching It Up to review how to build menu of functions
## Pandemic Board Game Port

During the Covid-19 Pandemic of Spring 2020, various browser-based ports of popular board games started making the rounds, 
so that one could play games over video conference with one's friend group while in lockdown. However my favorite board game, 
and one that felt deliciously ironic during this time, was missing from the list: Pandemic.

I decided creating my own port of the cooperative board game would be a good portfolio project to work on my budding web development skill.

### TODOs:

#### Front-End: (7)
** Design elements / HTML / CSS Layout: (6)
    ** Lines between cities
    - Player cards and cardbacks
    - City cards and cardbacks
    - Event cards
    - Epidemic cards
    - Outbreak Count
    - Infection Count
    - Player markers
    - Research stations
    - Disease markers
    - Player "nametag" and role name
    - Hint box
    - City name (animate in from left on hover)
- Continue plotting map markers (42 cities) (1)

#### Back-End: (10)
** City Test (1 method) (0.5)
** Refactor Disease into a Sequelize Model (0.5)
- City Model (0.5)
- Instantiate all the Cities (1)
- Player Test (8 methods) (2)
- Player Model (2)
- Game setup script (2)
- Gameplay script (2)

#### DOM: (5)
- Connect the JS Models to the DOM elements

##### Future Work:

###### Phase 2: Improvements
- Build 7 Player subclasses
- Build 5 Event subclasses

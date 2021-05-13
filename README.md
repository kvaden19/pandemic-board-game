## Pandemic Board Game Port

During the Covid-19 Pandemic of Spring 2020, various browser-based ports of popular board games started making the rounds, 
so that one could play games over video conference with one's friend group while in lockdown. However my favorite board game, 
and one that felt deliciously ironic during this time, was missing from the list: Pandemic.

I decided creating my own port of the cooperative board game would be a good portfolio project to work on my budding web development skills.

### TODOs:

#### Front-End: (7)
** Design elements / HTML / CSS Layout:
    - City name (animate in from left on hover)
    - Player cards
    - Player cardback
    - City cards
    - City cardback
    - Event cards
    - Epidemic cards (alert-like)
    - Outbreak Count
    - Infection Count
    - Player markers
    - Research stations
    - Disease markers
    - Player "nametag" and role name
    - Hint box
    - Player action menu
- Plot remaining City markers and routes using SVG

#### Back-End: (10)
- Rewrite Disease test to work with Sequelize model -- getting errors. Revisit after working through this issue on Tech Blog.
- City Test (1 method) (0.5)
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
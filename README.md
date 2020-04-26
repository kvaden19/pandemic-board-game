## **Pandemic Board Game Port**

During the Covid-19 Pandemic of Spring 2020, various browser-based ports of popular board games started making the rounds, 
so that one could play games over video conference with one's friend group while in lockdown. However my favorite board game, 
and one that felt deliciously ironic during this time, was missing from the list: Pandemic.

I decided creating my own port of the cooperative board game would be a good portfolio project to work on my budding Python 
and data science skills.

TASK LIST:
Phase 1: Text based game that 2 or more humans can pass + play.
- Write MVP game (no Events, no Roles, and no one is trying to break it).
- [X] Modify Player.treat and City.infect methods
- [ ] Write Game methods
- [ ] Write Play script
- [ ] Re-do unit tests with immutable default args + unit test new methods
- [ ] Improve placement and color of map annotations.
- [ ] Finish building out map.
- [ ] Code all the City objects
- User testing
- Read style guide and incorporate
- Add error checking
- Build 7 Player subclasses
- Build 5 Event subclasses

Phase 2: Deploy an console-based Python app over the web and have it collect data
- Build a data pipeline
- Play / share / accumulate data

Phase 3: Build a ML-based automated player

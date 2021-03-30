'''
Author: kvaden
10 April 2020
v1.0
'''

class Disease:
    def __init__(self, color=None, cured=False, eradicated=False):
        self.color = color
        self.cured = cured
        self.eradicated = eradicated

    def __str__(self):
        return 'The {} disease. Cured: {}. Eradicated: {}.'.format(self.color, self.cured, self.eradicated)
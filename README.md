#
# KR knight survivability simulator
#
# By Dfrever
#

'''
        DISCLAIMER

This is intended as a very specific testing tool specifically for knight class passive survivability
without accounting for class specific bonuses.

'''

This is a python script based on the simulator.py file (which calls the other modules).
Run simulator.py to perform simulations and edit source code for the different options.

The global variables:

NumRunsPerHero = 1000
SELECTIVE = 1
EXAUSTIVE = 0
FOCUSED = 0
PRINTALL = 1
STATCOMPARISON = 0

In simulator.py contain the bulk of possible variations.

Additional selective tank tests must be added to customHero.py, 
and to test different attacker parameters these must be altered at attacker.py.

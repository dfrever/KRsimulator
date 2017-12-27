#!/usr/bin/python

import itertools
import random
#custom modules
from hero import Hero, createHeroShell
from massGenHero import generateHeroes
from customHero import getCustomHeroes
from statComparison import compareStats
from attacker import Attacker

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
#########   TO-DO list         #########################
#- Organize the code. modulerize, separate specific hero entries to another file. -Meh, more or less
#--- Improve stat conversion code for block and toughness -OK
#--- Add T1 perk stats to simulation -OK
#- Allow simulation to contemplate differente gear quality/awakening
#- Simulate non UW weapons and compare them (with relative ease) -OKish - works on selective. Not for bulk creation.
#- IMPORTANT: Allow comparison of bulk simulation TTL by stat (plot graphs) for analytical conclusions on stat effectiveness
#- IMPORTANT: implement penetration for better knowledge of the importance of defense against high pen enemies
#--- IMportant: implement dmg smoothness measure (largest dmg avg for N consecutive hits -N = ? 3? 5?) - OK-ish

#-------------------------Attacker Declaration-----------------
attacker = Attacker()
#------------------------ Constants for simulation settings-------------------------
NumRunsPerHero = 1000
SELECTIVE = 1
EXAUSTIVE = 0
FOCUSED = 0
PRINTALL = 1
STATCOMPARISON = 0



#---------------------------Hero building------------------------

heroes = []


#-------------------------------Custom testing method ---------------------------------------
if SELECTIVE:
    heroes = getCustomHeroes(heroes, FOCUSED)


#-----------------------------Exaustive testing method -----------------------------------------
#Generates all possible combinations of hero stats
if EXAUSTIVE:
    heroes = generateHeroes(heroes)
    
#-----------------------------Simulation------------------------

#recieves hero and returns how many attacks he withstood
def toTheDeath(hero):
    turnCount = 0
    while hero.stats['hp'] > 0:
        turnCount = turnCount + 1
        #print "b4:", hero.stats["hp"]
        dmg = hero.getHit(attacker)
        #print "dmg:", dmg
        hero.stats["hp"] -= dmg
        #print "aft:", hero.stats["hp"]
    return turnCount

N = NumRunsPerHero #number of runs to test on each hero 

#j=0
for hero in heroes:
    #hit him till he dies N times, get average and variance measure
    sumTurns = 0
    #print "hero ", j
    for i in range(0,N):
        #beat em up
        t = toTheDeath(hero)
        hero.numSimulations += 1
        #recover him for new simulation
        hero.resetHeroHp()
        #update statistics
        sumTurns += t
        if t > hero.maxTurns:
            hero.maxTurns = t
        if t < hero.minTurns:
            hero.minTurns = t
    hero.avgTurns = sumTurns*1.0/N
    #j+=1    

#sort heroes by most turns survived and print
heroes.sort(reverse=True)
if (not EXAUSTIVE) and PRINTALL:
    print "Tested ", len(heroes), "combinations"
    for hero in heroes:
        hero.printStats()
        print '\n'
elif EXAUSTIVE and PRINTALL:
    print "Tested ", len(heroes), "combinations"
    for i in range(0, 10):
        heroes[i].printStats()
        print '\n'
elif not STATCOMPARISON:
    print "Tested ", len(heroes), "combinations"
    print "Best: "
    heroes[0].printStats() #"best"hero
    if len(heroes) >= 3 :
        print "second: "
        heroes[1].printStats() 
        print "third: "
        heroes[2].printStats()



#Stat comparison 
if STATCOMPARISON:
    attacker.crit = 0.0 #Force zero crit to remove noise from comparation
    compareStats(attacker)

   

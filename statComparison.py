#module statComparison
import matplotlib.pyplot as plt
from hero import Hero, createHeroShell, createHeroShellPBDefRune, createHeroShellPToughRune, createHeroShellRing, createHeroShellBracelet

#global for graph exibition
SHOWINDIVIDUAL = 0
SHOWGROUPED = 1

#recieves hero and returns how many attacks he withstood
def toTheDeath(hero, attacker):
    turnCount = 0
    while hero.stats['hp'] > 0:
        turnCount = turnCount + 1
        #print "b4:", hero.stats["hp"]
        dmg = hero.getHit(attacker)
        #print "dmg:", dmg
        hero.stats["hp"] -= dmg
        #print "aft:", hero.stats["hp"]
    return turnCount



#generate hero with baseline stats
#preform hit till death runs N times
#alter stat by increment I of interest and repeat
#gather all data for stat: TTL
#repeat for stat variations on all stats of interest
#be smart about variations: Example, make variations on gear-available substats for different UW rune configurations
#plot graphs
def compareStats(attacker):
    #N = NumRunsPerHero
    N = 30
    #h = createHeroShell()
    #h = createHeroShellRing()
    #h = createHeroShellBracelet()
    h = createHeroShellPBDefRune()
    #h = createHeroShellPToughRune()
    #print h.stats #initial stats
    #positive variations only
    pdefVariations = []
    defx = []
    defy1 = []
    defy2 = []
    #for i in range(0, 30): #+30K defense
    for i in range(0, 20):
        sumTurns = 0
        for i in range(0,N):
            #beat em up
            t = toTheDeath(h, attacker)
            h.numSimulations += 1
            #recover him for new simulation
            h.resetHeroHp()
            #h.resetAll()
            #h.largestSpike = 0
            #h.lastHits = []
            #update statistics
            sumTurns += t
            if t > h.maxTurns:
                h.maxTurns = t
            if t < h.minTurns:
                h.minTurns = t
        ttl = sumTurns*1.0/N
        #print h.largestSpike
        #print  h.largestSpike*1.0/h.stats['maxhp']
        maxSpike = h.largestSpike*1.0/h.stats['maxhp']
        pdefVariations.append([h.stats['pdef'], ttl, maxSpike])
        defx.append(h.stats['pdef'])
        defy1.append(ttl)
        defy2.append(maxSpike)
        #print "MAXSPIKE-D: ", maxSpike
        h.resetAll()
        #h.stats['pdef']+= 1000
        #h.stats['pdef']+= 941.5 #hp ring
        h.stats['pdef']+= 1441.5 #bracelet
    #print pdefVariations
    #return 0
    #h.printStats() 

    #remove former defense increments
    #h = createHeroShell()
    #h = createHeroShellRing()
    #h = createHeroShellBracelet()
    h = createHeroShellPBDefRune()
    #h = createHeroShellPToughRune()
    #blockVariations = []
    blx = []
    bly1 = []
    bly2 = []
    #for i in range(0, 30): #+1.5K block
    for i in range(0, 20):
        sumTurns = 0
        for i in range(0,N):
            #beat em up
            t = toTheDeath(h, attacker)
            h.numSimulations += 1
            #recover him for new simulation
            h.resetHeroHp()
            #update statistics
            sumTurns += t
            if t > h.maxTurns:
                h.maxTurns = t
            if t < h.minTurns:
                h.minTurns = t
        ttl = sumTurns*1.0/N

        maxSpike = h.largestSpike/h.stats['maxhp']
        #blockVariations.append([h.stats['pblock'], ttl, maxSpike])
        blx.append(h.stats['pblock'])
        bly1.append(ttl)
        bly2.append(maxSpike)
        h.resetAll()
        #h.stats['pblock']+= 50
        h.stats['pblock']+= 55 
        
    
    #remove former block increments
    #h = createHeroShell()
    #h = createHeroShellRing()
    #h = createHeroShellBracelet()
    h = createHeroShellPBDefRune()
    #h = createHeroShellPToughRune()
    #hpVariations = []
    hpx = []
    hpy1 = []
    hpy2 = []
    #for i in range(0, 30): #+3m hp
    for i in range(0, 20):
        sumTurns = 0
        for i in range(0,N):
            #beat em up
            t = toTheDeath(h, attacker)
            h.numSimulations += 1
            #recover him for new simulation
            h.resetHeroHp()
            #update statistics
            sumTurns += t
            if t > h.maxTurns:
                h.maxTurns = t
            if t < h.minTurns:
                h.minTurns = t
        ttl = sumTurns*1.0/N

        maxSpike = h.largestSpike/h.stats['maxhp']
        #hpVariations.append([h.stats['maxhp'], ttl, maxSpike])
        hpx.append(h.stats['maxhp'])
        hpy1.append(ttl)
        hpy2.append(maxSpike)
        h.resetAll()
        #h.stats['maxhp']+= 100000
        #h.stats['maxhp']+= 86275.5 #hp ring
        h.stats['maxhp']+= 51577.5 #bracelet
        h.stats['hp'] = h.stats['maxhp']

    #remove former hp increments
    #h = createHeroShell()
    #h = createHeroShellRing()
    #h = createHeroShellBracelet()
    h = createHeroShellPBDefRune()
    #h = createHeroShellPToughRune()
    #dodgeVariations = []
    dox = []
    doy1 = []
    doy2 = []
    #for i in range(0, 30): #1.5K dodge
    for i in range(0, 20):
        sumTurns = 0
        for i in range(0,N):
            #beat em up
            t = toTheDeath(h, attacker)
            h.numSimulations += 1
            #recover him for new simulation
            h.resetHeroHp()
            #update statistics
            sumTurns += t
            if t > h.maxTurns:
                h.maxTurns = t
            if t < h.minTurns:
                h.minTurns = t
        ttl = sumTurns*1.0/N

        maxSpike = h.largestSpike/h.stats['maxhp']
        #dodgeVariations.append([h.stats['pdodge'], ttl, maxSpike])
        dox.append(h.stats['pdodge'])
        doy1.append(ttl)
        doy2.append(maxSpike)
        h.resetAll()
        #h.stats['pdodge']+= 50
        h.stats['pdodge']+= 27.5
    #testing
    #print "dodge spike: ",doy2
    #print "hp spike: ", hpy2
    #print "def spike:", defy2
    #print "bl spike:", bly2


    #plotting graphs:  
    if SHOWINDIVIDUAL: 
        
        #TTL  for def
        plt.plot(defx, defy1)
        #plt.legend(('ttl'),loc = 0)
        plt.xlabel('def')
        plt.ylabel('ttl')
        plt.grid(True)
        plt.show()
        #spike for def
        plt.plot(defx, defy2)
        #plt.legend(('spike'),loc = 0)
        plt.xlabel('defense')
        plt.ylabel('spike in % maxhp')
        plt.grid(True)
        plt.show()

        #TTL  for hp
        plt.plot(hpx, hpy1)
        #plt.legend(('ttl'),loc = 0)
        plt.xlabel('hp')
        plt.ylabel('ttl')
        plt.grid(True)
        plt.show()
        #spike for hp
        plt.plot(hpx, hpy2)
        #plt.legend(('spike'),loc = 0)
        plt.xlabel('hp')
        plt.ylabel('spike in % maxhp')
        plt.grid(True)
        plt.show()

        #TTL  for block
        plt.plot(blx, bly1)
        #plt.legend(('ttl'),loc = 0)
        plt.xlabel('block')
        plt.ylabel('ttl')
        plt.grid(True)
        plt.show()
        #spike for block
        plt.plot(blx, bly2)
        #plt.legend(('spike'),loc = 0)
        plt.xlabel('block')
        plt.ylabel('spike in % maxhp')
        plt.grid(True)
        plt.show()

        #TTL  for dodge
        plt.plot(dox, doy1)
        #plt.legend(('ttl'),loc = 0)
        plt.xlabel('dodge')
        plt.ylabel('ttl')
        plt.grid(True)
        plt.show()
        #spike for dodge
        plt.plot(dox, doy2)
        #plt.legend(('spike'),loc = 0)
        plt.xlabel('dodge')
        plt.ylabel('spike in % maxhp')
        plt.grid(True)
        plt.show()    
             
    if SHOWGROUPED:
        #inc = range(0,30)
        inc = range(0,20)
        #ttl mixed:
        plt.plot(inc, doy1)
        plt.plot(inc, bly1)
        plt.plot(inc, defy1)
        plt.plot(inc, hpy1)
        plt.legend(('dodge', 'block', 'defense', 'hp'),loc = 0)
        plt.xlabel('increments')
        plt.ylabel('ttl')
        plt.grid(True)
        plt.show()

        #smoothness mixed:
        plt.plot(inc, doy2)
        plt.plot(inc, bly2)
        plt.plot(inc, defy2)
        plt.plot(inc, hpy2)
        plt.legend(('dodge', 'block', 'defense', 'hp'),loc = 0)
        plt.xlabel('increments')
        plt.ylabel('spike')
        plt.grid(True)
        plt.show()


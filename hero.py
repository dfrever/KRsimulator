#module hero
import random
from statDR import calcBlockChance, calcDodgeChance, calcBlockDef, calcTough


DEBUG = 0

#---------------------------Hero ---------------------------------

class Hero:
    def __init__(self, maxhp=0,hp=1354584+912556, att=15712, pdef=6984+27251, mdef=5432+27251, pblock=200, mblock=0,ptough=250, mtough=250, pblockdef=0, mblockdef=0, pdodge=0, mdodge=0):
        self.stats = {'name': 'undefined', 'hp': hp, 'att':att, 'pdef': pdef, 'mdef': mdef, 'pblock': pblock, 'mblock': mblock, 'pblockdef': pblockdef,'mblockdef': mblockdef, 'ptough': ptough,  'mtough': mtough, 'pdodge': pdodge,  'mdodge': mdodge, 'maxhp': maxhp}
        self.gear = []
        #counters for result exibition (of bulk simulations - not reset by resetHero)
        self.totalAttackCounter = 0
        self.totalPhisCounter = 0
        self.totalMagicCounter = 0
        self.blockedCounter = 0
        self.dodgedCounter = 0
        self.gotCritCounter = 0
        self.numSimulations = 0
        #reset every simulation
        self.lastHits = []
        self.spikeSequenceSize = 5
        self.largestSpike = 0
        #survivability in simulation
        self.avgTurns = 0
        self.maxTurns = 0
        self.minTurns = 200000
        self.printed = 0 #debugging

    #comparision definition for hero class to sort by survivability
    def __lt__(self, other):
         return self.avgTurns < other.avgTurns
    
    def resetHeroHp(self):
        self.stats['hp']  = self.stats['maxhp']


    def resetAll(self):
        self.totalAttackCounter = 0
        self.totalPhisCounter = 0
        self.totalMagicCounter = 0
        self.blockedCounter = 0
        self.dodgedCounter = 0
        self.gotCritCounter = 0
        self.numSimulations = 0
        self.lastHits = []
        self.spikeSequenceSize = 5
        self.largestSpike = 0
        self.avgTurns = 0
        self.maxTurns = 0
        self.minTurns = 200000
        self.stats['hp']  = self.stats['maxhp']
        self.printed = 0

    def printStats(self):
        print "HERO: ", self.stats['name']
        print "Avg turns survived: ", self.avgTurns, "(Min: ", self.minTurns,", Max: ",self.maxTurns,")"
        print "Largest Spike (for a",self.spikeSequenceSize," hit sequence): ", '{0:3.1f}'.format(self.largestSpike/self.stats['maxhp']*100), "% of hp"
        print "in ", self.numSimulations, " runs: " 
        print "    total times attacked: ", self.totalAttackCounter, "(",self.totalPhisCounter," phis, ", self.totalMagicCounter," magical)"
        print "    total blocked hits: ", self.blockedCounter, " (avg: ", self.blockedCounter/self.numSimulations," per run)"
        print "    total dodged hits: ", self.dodgedCounter, " (avg: ", self.dodgedCounter/self.numSimulations," per run)"
        #print "test: ", self.getPDodgeChance()
        UWRunes = []
        gear = self.gear
        for item in gear:
            if item[2] == "WRune":
                UWRunes.append(item)
        print "UW runes: ", UWRunes
        for item in gear:
            if item[2] == "PRune":
                print "Primary Rune: ", item
            if item[2] == "SRune":
                print "Secondary Rune: ", item
            if item[2] == "perk":
                print "T1 Perk: ", item[0]
        lines=[["hp%", 0], ["pdef%", 0],["mdef%", 0], ["pdodge", 0], ["pblock", 0]]
        for line in gear:
            if line[2] == "sub":
                for l in lines:
                    if l[0] == line[0]:
                        l[1] +=1
            if line[2] == "ring":
                print "wearing ring"
            if line[2] == "bracelet":
                print "wearing bracelet"
            if line[2] == "amulet":
                print "wearing amulet"
        print "substat lines: ", lines
        

        #print "final stats", self.stats

    #returns damage taken from a single attack
    def getHit(self, attacker):
        self.totalAttackCounter +=1
        #type determination for random case
        currentType = 2
        if (attacker.type == 'b'):
            currentType = random.randint(0,1)
        if attacker.type == 'p' or currentType == 0 :
            currentType = 0
            self.totalPhisCounter +=1
        if attacker.type == 'm' or currentType == 1 :
            currentType = 1
            self.totalMagicCounter +=1
        #avoidance check
        if (self.avoidance(currentType)):
            self.dodgedCounter+=1
            return 0
        #crit check
        crit = 0
        if (random.random() < attacker.crit):
            crit = 1
            self.gotCritCounter+=1
        #block check
        block = 0
        if (self.block(currentType)):
            block = 1
            self.blockedCounter+=1

        #damage resolution
        tough, defReduc = self.getMitigation(currentType)
        if crit:
            dmg = attacker.att*(2+attacker.critDmg)*defReduc*tough
        else :
            dmg = attacker.att*defReduc*tough
        if block:
            blockMitigation = self.blockMitigation(currentType)
            dmg = dmg*blockMitigation

        if not self.printed and DEBUG: 
            print "dmg: ", dmg, "  def:", self.stats['pdef'], '  defRed: ', defReduc, '   tough: ',tough
            self.printed = 1
        #updating smoothness counters
        self.lastHits.append(dmg)
        if len(self.lastHits) >= self.spikeSequenceSize:
            self.lastHits.pop(0)
            if self.largestSpike < sum(self.lastHits):
                self.largestSpike = sum(self.lastHits)
                #print sum(self.lastHits)
        return dmg
        

    #returns dmg reduction factor for a block given dmg type
    def blockMitigation(self, currentType):
        if (currentType == 0):
            reduct = self.pBlockReduct()
        elif (currentType == 1):
            reduct = self.mBlockReduct()
        return reduct
    
    def pBlockReduct(self):
        return calcBlockDef(self.stats["pblockdef"]) #same formula for toughness

    def mBlockReduct(self):
        return calcBlockDef(self.stats["mblockdef"]) #same formula for toughness

    #removes accuracy from dodge and transforms to decimal for operations
    def pAvoidChance(self):
        #return (self.getPDodgeChance() - attacker.acc)*1.0 #accuracy not implemented
        return self.getPDodgeChance()
    def mAvoidChance(self):
        #return (self.getMDodgeChance() - attacker.acc)*1.0 #accuracy not implemented
        return self.getMDodgeChance()
    #deals with avoidance roll for any attack type
    def avoidance(self, currentType):
        if (currentType == 0):
            chance = self.pAvoidChance()
        elif (currentType == 1):
            chance = self.mAvoidChance()
        roll = random.random()
        if roll <= chance:
            return 1 #true - avoids
        else: 
            return 0 

    #returns dodge chance (not in decimal form)
    def getPDodgeChance(self):
        return calcDodgeChance(self.stats['pdodge'])
      
    def getMDodgeChance(self):
        return calcDodgeChance(self.stats['mdodge'])

    def block(self, currentType):
        if (currentType == 0):
            chance = self.getPblockChance()
        elif (currentType == 1):
            chance = self.getMblockChance()
        roll = random.random()
        if roll <= chance:
            return 1 #true - avoids
        else: 
            return 0 

    def getPblockChance(self):
        return calcBlockChance(self.stats['pblock'])
     
    def getMblockChance(self):
        return calcBlockChance(self.stats['mblock'])
      

    def getMitigation(self, currentType):
        defRed = 1
        if (currentType == 0):
            defRed = 1- self.pdefMitigation()*1.0
            tough = calcTough(self.stats["ptough"])
        elif (currentType == 1):
            defRed = 1- self.mdefMitigation()*1.0
            tough = calcTough(self.stats["mtough"])
        return tough, defRed

    
    #these return defense dmg reduction. To use, remember to use 1-mit for amount of passing dmg
    def pdefMitigation(self):
        temp = 0.0

        # coefficients
        #a = 9.8422403011163961E-01
        #b = 9.6815105603447773E+03
        a= 0.9842
        b= 9681.5

        temp = (a * self.stats['pdef']) / (b + self.stats['pdef'])
        return temp

    def mdefMitigation(self):
        temp = 0.0

        # coefficients
        #a = 9.8422403011163961E-01
        #b = 9.6815105603447773E+03
        a= 0.9842
        b= 9681.5

        temp = (a * self.stats['mdef']) / (b + self.stats['mdef'])
        return  temp

    #def getTotalPMitigation(self):
    #    return self.stats['ptough'] * self.pdefMitigation()

    #def getTotalMMitigation(self):
    #     return self.stats['mtough'] * self.mdefMitigation()



#----------------------Creates hero instance -------------------------------------

#Should i fit this in hero initialization?

def createHero(statList):
    hero = Hero()
    percentages = []
    cleanList = []
    perkBonus = []
    #Perks in % effect, base = 100%
    hpperk =  100
    pdefperk = 100
    mdefperk = 100
    #print statList
    hero.gear = statList
    for s in statList:
        #hero.gear.append(s)
        if '%' in s[0]:
            if s[2] == 'perk':
                #percentages.append(s) #if perk behaves as regular substat
                perkBonus = s #if applies over total must be separate
            else :
                percentages.append(s)
        elif s[2] == 'name':
            hero.stats['name'] =  s[0]
            continue
        elif "none" in s[0]:
            continue
        else:
            cleanList.append(s)
    #apply basic flat bonuses
    for s in cleanList:
        hero.stats[s[0]] = hero.stats[s[0]] + s[1]
    #sum percentage bonuses
    hpp = 0
    pdefp = 0
    mdefp = 0
    for p in percentages:
        if p[0] == 'hp%':
            hpp = hpp + p[1]
        elif  p[0] == 'mdef%':
            mdefp = mdefp + p[1]
        elif  p[0] == 'pdef%':
            pdefp = pdefp + p[1]

    if perkBonus[0] == 'hp%':
        hpperk += perkBonus[1]
    elif  perkBonus[0] == 'mdef%':
        mdefperk += perkBonus[1]
    elif  perkBonus[0] == 'pdef%':
        pdefperk += perkBonus[1]

    #apply percentage bonuses
    hpp = hpp/100.0 + 1.0
    pdefp = pdefp/100.0 + 1.0
    mdefp = mdefp/100.0 + 1.0
    #print "tessst"
    #print "hp percents:", hpp, ", pdef percents:",pdefp
    #print "hp perk: ",hpperk, ", pdef perk: ", pdefperk
    hero.stats['hp'] = (hero.stats['hp']*hpp)*(hpperk*1.0/100)
    hero.stats['maxhp'] = hero.stats['hp']
    hero.stats['pdef'] = (hero.stats['pdef']*pdefp)*(pdefperk*1.0/100)
    hero.stats['mdef'] = (hero.stats['mdef']*mdefp)*(mdefperk*1.0/100)

    return hero


def createHeroShell():
    h =Hero()
    h.stats['maxhp'] = h.stats['hp']
    return h

def createHeroShellRing():
    h =Hero()
    h.stats['hp'] += 870153
    h.stats['maxhp'] = h.stats['hp']
    return h

def createHeroShellBracelet():
    h =Hero()
    h.stats['pdef'] +=18182
    h.stats['maxhp'] = h.stats['hp']
    return h


def createHeroShellPBDefRune():
    h =Hero()
    h.stats['pblockdef'] = 200
    h.stats['pblock'] = 700
    h.stats['pdef'] +=18182
    #h.stats['hp'] += 870153
    h.stats['maxhp'] = h.stats['hp']
    return h


def createHeroShellPToughRune():
    h =Hero()
    h.stats['ptough']+= 200
    h.stats['maxhp'] = h.stats['hp']
    return h




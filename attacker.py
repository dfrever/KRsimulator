#module attacker



class Attacker:
    def __init__(self):
        self.acc = 0      #not implemented
        self.att = 1000000.0
        self.crit = 0.10  #crit chance in decimal
        self.critDmg = 0
        self.pen = 0        #uninplemented
        self.type = 'p' #p for phisical, m for magical, b to use both randomly (simulate mixed attacks)
    def printStats(self):
        print "Att: ", self.att
        print "Crit: ", self.crit
        print "critDmg:", self.critDmg

#module massGenHero
import itertools
from hero import createHero


# -----------------Rune options and substats considered---------------

#3 UW slots - options: Ptough (200), mtough(200), PblockDef(200), MblockDef(200), mana/att(?consider it)
#1 main armor slot - options: 20% maxHP, 40%Pdef, 40%Mdef, 200 Pblock, 200Mblock
#1 sub armor rune slot - options: 200 Pdodge, 200 Mdodge, Mana-Recovery/Dmg

#4 sets of substats - options: pdef, mdef, hp, pblock, (cc resist/ att spd??) 
####tecnicly there are only 4 relevant defensive subs. Test 3 out of 4 and 2 out of 4 impact in survivability (for options to other subs non-related do surviving passively).

#max substat values(at t7): pdef 11%, mdef 11%, hp:11%, pblock:220, pdodge 110

#------------------Game Stat info------------------
#t7 5* BP pdef:27251
#t7 5* shield mdef: 27251
#t7 5* orb hp: 912556

#t7 5* ring HP: 870153
#t7 5* bracelet pdef: 18182 (found one)
#t7 5* amulet mdef: 18182 (assumption)


#Note: frost set is 10%/13% hp - Not being used atm


def generateHeroes(heroes, subsPerPiece = 4): 
    #generate heroes with all possible combinations of runes, options and gear choices

    #all rune combinations
    wrunes =  [["ptough", 200, "WRune"],["mtough",200, "WRune"],["pblockdef", 200, "WRune"],["mblockdef",200, "WRune"], ["none",0, "WRune"]]
    weaps = []
    #for wruneA in wrunes:
    #    for wruneB in wrunes:
    #        for wruneC in wrunes:
    #            weaponPossilities.append([wruneA, wruneB, wruneC])
    weaponPossilities = []
    weaps = list(itertools.combinations(wrunes, 3))
    for l in weaps:
        weaponPossilities.append(list(l))
    print "Weapon Rune combinations complete."
    #print weaponPossilities

    prunes =  [["hp%", 20, "PRune"], ["pdef%", 40, "PRune"], ["mdef%", 40, "PRune"], ["pblock", 200, "PRune"], ["mblock", 200, "PRune"], ["none",0, "PRune"]]
    weapAndPcomb = []
    for w in weaponPossilities:
        for p in prunes:
            weapAndPcomb.append(w + [p])
    print "Primary combinations added."
    #weapAndPcomb = combinations(prunes, )

    allRuneComb = []
    srunes =  [["pdodge", 200, "SRune"],["mdodge",200, "SRune"], ["none",0, "SRune"]]
    for c in weapAndPcomb:
        for s in srunes:
            allRuneComb.append(c + [s])
    print "Secondary combinations added."
    #print allRuneComb[0]
    #all accessory combinations
    accessories = [["hp", 870153, "ring"], ["pdef", 18182, "bracelet"], ["mdef", 18182, "amulet"]]

    #possible T1 perks
    perks = [["hp%", 30, "PRune"], ["pdef%", 50, "PRune"], ["mdef%", 50, "PRune"]]

    # UW and weapon combinations
    #ignoring for now, would have to add additional loop for substat options cominations...

    #substat line combinations 16 total (UW)
    #for ALL possible combinations, including non-def (none) slots (computationaly heavy):
    #substats =  [["pdef%", 11], ["mdef%", 11], ["hp%",11], ["pblock",220] , ["pdodge", 110], ["none", 0],["none", 0], ["none", 0], ["none", 0]]
    substats =  [["pdef%", 11, "sub"], ["pdodge", 110, "sub"], ["mdef%", 11, "sub"], ["hp%",11, "sub"], ["pblock",220, "sub"], ["none", 0, "sub"]]

    totalcombs = []
    #need to replicate for it to iterate the same subcombination repeated
    print "Generating all item builds: "
    #This should be more precise to combine all possible combinations, but requires to much memory.
    subsTimesFour = substats + substats + substats + substats
    for x in itertools.combinations(subsTimesFour,16):
        totalcombs.append(list(x))

    #LIMITED VERSION:
    #combinations of 4x repetition of a stat.
    #for x in itertools.combinations(substats, subsPerPiece):
    #    totalcombs.append(list(x)+list(x)+list(x)+list(x))
    print "Substat combinations complete (", len(totalcombs), ")."


    '''
    #subcombinations = itertools.permutations(substats, subsPerPiece)
    #totalcombs = itertools.permutations(subcombinations)

    subcombinations = itertools.combinations(substats, subsPerPiece)
    #print subcombinations
    temptotalcombs = itertools.combinations(list(subcombinations), subsPerPiece)
    #print list(totalcombs)
    for t in temptotalcombs:
        subcombs = []
        for s in t:
            #subcombs.append(list(s))
            totalcombs.append(list(s))
        #totalcombs.append(list(subcombs))
    #totalcombs = list(totalcombs)

    
   

   
    #quick fix compromise. Builds ARE being overlooked.
    subcombinations1 = itertools.combinations(substats, subsPerPiece)
    subcombinations2 = itertools.combinations(substats, subsPerPiece)
    subcombinations3 = itertools.combinations(substats, subsPerPiece)
    subcombinations4 = itertools.combinations(substats, subsPerPiece)

    for sub1 in subcombinations1:
        for sub2 in subcombinations2:
            for sub3 in subcombinations3:
                for sub4 in subcombinations4:   
                    totalcombs.append(list(sub1 + sub2 + sub3 + sub4))    
     '''
    allGearSettings = []
    for runeSet in allRuneComb:
        for subCombo in totalcombs:
            for access in accessories:
                for perk in perks:
                    #print runeSet[0] 
                    #print subCombo[0] 
                    #print access[0]
                    allGearSettings.append(runeSet + list(subCombo) + [access] + [perk])
                    #allGearSettings.append(runeSet + subCombo + [access])
    print "All item builds Generated."
    #generating all heroes for gear stat combinations
    for gset in allGearSettings:
        heroes.append(createHero(gset))
    print "All Heroes Generated(",len(heroes),")."
    #return heroes


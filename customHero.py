#module customHero
from hero import createHero


#-------------------------------Custom testing method ---------------------------------------
#recieves hero list, appends custom heroes.
def getCustomHeroes(heroes, focusedHeroes):
    if focusedHeroes:
        #block inclined
        blockSet = [
                ['none', 0, 'WRune'], ['none', 0, 'WRune'], ['pblockdef', 200, 'WRune'], #UW runes
                ['pblock', 200, 'PRune'],                       # primary rune
                ['none', 0, 'SRune'],                   #secondary rune
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['pblock', 220, 'sub'], 
                ['hp', 870153, 'ring'],                    #accessory
                ['hp%', 30, 'perk'],                       #T1 perk
                ['blockset',0, 'name']
        ]
        heroes.append(createHero(blockSet))
        #dodge inclined
        dodgeSet = [
                ['none', 0, 'WRune'], ['none', 0, 'WRune'], ['none', 0, 'WRune'], #UW runes
                ['none', 0, 'PRune'],                             # primary rune
                ['pdodge', 200, 'SRune'],                   #secondary rune
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['pdodge', 110, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['pdodge', 110, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['pdodge', 110, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['pdodge', 110, 'sub'], 
                ['hp', 870153, 'ring'],                    #accessory
                ['hp%', 30, 'perk'],                       #T1 perk
                ['dodgeset',0, 'name']
        ]
        heroes.append(createHero(dodgeSet))
        #p defense inclined
        pdefSet = [
                ['none', 0, 'WRune'], ['none', 0, 'WRune'], ['none', 0, 'WRune'], #UW runes
                ['pdef%', 40, 'PRune'],                             # primary rune
                ['none', 0, 'SRune'],                   #secondary rune
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['pdef%', 11, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['pdef%', 11, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['pdef%', 11, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['pdef%', 11, 'sub'], 
                ['pdef', 18182, 'bracelet'],                    #accessory
                ['pdef%', 50, 'perk'],                       #T1 perk
                ['pdefset',0, 'name']
        ]
        heroes.append(createHero(pdefSet))

        #m defense inclined
        mdefSet = [
                ['none', 0, 'WRune'], ['none', 0, 'WRune'], ['none', 0, 'WRune'], #UW runes
                ['mdef%', 40, 'PRune'],                             # primary rune
                ['none', 0, 'SRune'],                   #secondary rune
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['mdef%', 11, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['mdef%', 11, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['mdef%', 11, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['mdef%', 11, 'sub'], 
                ['mdef', 18182, 'amulet'],                    #accessory
                ['mdef%', 50, 'perk'],                       #T1 perk
                ['mdefset',0, 'name']
        ]
        heroes.append(createHero(mdefSet))


        #hp inclined
        hpSet = [
                ['none', 0, 'WRune'], ['none', 0, 'WRune'], ['none', 0, 'WRune'], #UW runes
                ['hp%', 20, 'PRune'],                             # primary rune
                ['none', 0, 'SRune'],                   #secondary rune
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['hp%', 11, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['hp%', 11, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['hp%', 11, 'sub'], 
                ['none', 0, 'sub'], ['none%', 0, 'sub'], ['none', 0, 'sub'], ['hp%', 11, 'sub'], 
                ['hp', 870153, 'ring'],                    #accessory
                ['hp%', 30, 'perk'],                       #T1 perk
                ['hpset',0, 'name']
        ]
        heroes.append(createHero(hpSet))


    #-----------------------------Actual functional sets
    else:
        BaseStat = [
                ['none%', 0, 'perk'],
                ['BaseStat',0, 'name']
        ]
        heroes.append(createHero(BaseStat))
  
        MaxPhysical1B = [
                ['ptough', 200, 'WRune'], ['ptough', 200, 'WRune'], ['pblockdef', 200, 'WRune'], #UW runes
                ['pdef%', 40, 'PRune'],                       # primary rune
                ['pdodge', 200, 'SRune'],                   #secondary rune
                ['pdef%', 11, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['pdef%', 11, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['pdef%', 11, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['pdef%', 11, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['pdef', 18182, 'bracelet'],                   #accessory
                ['pdef%', 50, 'perk'],                       #T1 perk
                ['MaxPhysical1B',0, 'name']
        ]
        heroes.append(createHero(MaxPhysical1B))

        GeneralUWRing = [
                ['mtough', 200, 'WRune'], ['ptough', 200, 'WRune'], ['pblockdef', 200, 'WRune'], #UW runes
                ['hp%', 20, 'PRune'],                       # primary rune
                ['pdodge', 200, 'SRune'],                   #secondary rune
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['hp', 870153, 'ring'],                   #accessory
                ['hp%', 30, 'perk'],                       #T1 perk
                ['GeneralUWRing',0, 'name']
        ]
        heroes.append(createHero(GeneralUWRing))

        MaxEHPUWRing = [
                ['mtough', 200, 'WRune'], ['ptough', 200, 'WRune'], ['pblockdef', 200, 'WRune'], #UW runes
                ['hp%', 20, 'PRune'],                       # primary rune
                ['pdodge', 200, 'SRune'],                   #secondary rune
                ['none', 0, 'sub'], ['pdef%', 11, 'sub'], ['hp%', 11, 'sub'], ['mdef%', 11, 'sub'], 
                ['none', 0, 'sub'], ['pdef%', 11, 'sub'], ['hp%', 11, 'sub'], ['mdef%', 11, 'sub'], 
                ['none', 0, 'sub'], ['pdef%', 11, 'sub'], ['hp%', 11, 'sub'], ['mdef%', 11, 'sub'], 
                ['none', 0, 'sub'], ['pdef%', 11, 'sub'], ['hp%', 11, 'sub'], ['mdef%', 11, 'sub'], 
                ['hp', 870153, 'ring'],                   #accessory
                ['hp%', 30, 'perk'],                       #T1 perk
                ['MaxEHPUWRing',0, 'name']
        ]
        heroes.append(createHero(MaxEHPUWRing))

        MaxEHPUWBraceletDefP = [
                ['mtough', 200, 'WRune'], ['ptough', 200, 'WRune'], ['pblockdef', 200, 'WRune'], #UW runes
                ['def%', 40, 'PRune'],                       # primary rune
                ['pdodge', 200, 'SRune'],                   #secondary rune
                ['none', 0, 'sub'], ['pdef%', 11, 'sub'], ['hp%', 11, 'sub'], ['mdef%', 11, 'sub'], 
                ['none', 0, 'sub'], ['pdef%', 11, 'sub'], ['hp%', 11, 'sub'], ['mdef%', 11, 'sub'], 
                ['none', 0, 'sub'], ['pdef%', 11, 'sub'], ['hp%', 11, 'sub'], ['mdef%', 11, 'sub'], 
                ['none', 0, 'sub'], ['pdef%', 11, 'sub'], ['hp%', 11, 'sub'], ['mdef%', 11, 'sub'], 
                ['pdef', 18182, 'bracelet'],                    #accessory
                ['def%', 50, 'perk'],                       #T1 perk
                ['MaxEHPUWBraceletDefP',0, 'name']
        ]
        heroes.append(createHero(MaxEHPUWBraceletDefP))

        GeneralNoUWRing = [
                ['mtough', 200, 'WRune'],                   #UW runes
                ['hp%', 20, 'PRune'],                       # primary rune
                ['pdodge', 200, 'SRune'],                   #secondary rune
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['hp', 870153, 'ring'],                   #accessory
                ['hp%', 30, 'perk'],                       #T1 perk
                ['GeneralNoUWRing',0, 'name']
        ]
        heroes.append(createHero(GeneralNoUWRing))
        '''
        GeneralUWRingPump = [
                ['mtough', 200, 'WRune'], ['ptough', 200, 'WRune'], ['pblockdef', 200, 'WRune'], #UW runes
                ['mblock', 300, 'WRune'],
                ['hp%', 20, 'PRune'],                       # primary rune
                ['pdodge', 200, 'SRune'],                   #secondary rune
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['hp', 870153, 'ring'],                   #accessory
                ['hp%', 50, 'perk'],                       #T1 perk
                ['GeneralUWRingPump',0, 'name']
        ]
        heroes.append(createHero(GeneralUWRingPump))

        GeneralUWRingMBL = [
                ['mtough', 200, 'WRune'], ['ptough', 200, 'WRune'], ['pblockdef', 200, 'WRune'], #UW runes
                ['mblock', 600, 'WRune'], ['mblockdef', 100, 'WRune'],  #BONUS CHEATZOR
                ['hp%', 20, 'PRune'],                       # primary rune
                ['pdodge', 200, 'SRune'],                   #secondary rune
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['hp', 870153, 'ring'],                   #accessory
                ['hp%', 30, 'perk'],                       #T1 perk
                ['GeneralUWRingMBL',0, 'name']
        ]
        heroes.append(createHero(GeneralUWRingMBL))
        
        GeneralUWRingMD = [
                ['mtough', 200, 'WRune'], ['ptough', 200, 'WRune'], ['pblockdef', 200, 'WRune'], #UW runes
                ['hp%', 20, 'PRune'],                       # primary rune
                ['mdodge', 200, 'SRune'],                   #secondary rune
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['none', 0, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['hp', 870153, 'ring'],                   #accessory
                ['hp%', 30, 'perk'],                       #T1 perk
                ['GeneralUWRingMD',0, 'name']
        ]
        heroes.append(createHero(GeneralUWRingMD))

        FullGeneralUWRing = [
                ['mtough', 200, 'WRune'], ['ptough', 200, 'WRune'], ['pblockdef', 200, 'WRune'], #UW runes
                ['hp%', 20, 'PRune'],                       # primary rune
                ['pdodge', 200, 'SRune'],                   #secondary rune
                ['pdef%', 11, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['pdef%', 11, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['mdef%', 11, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['mdef%', 11, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['hp', 870153, 'ring'],                   #accessory
                ['hp%', 30, 'perk'],                       #T1 perk
                ['FullGeneralUWRing',0, 'name']
        ]
        heroes.append(createHero(FullGeneralUWRing))

        FullGeneralUWRingMBL = [
                ['mtough', 200, 'WRune'], ['ptough', 200, 'WRune'], ['pblockdef', 200, 'WRune'], #UW runes
                ['mblock', 600, 'WRune'], ['mblockdef', 100, 'WRune'],  #BONUS CHEATZOR
                ['hp%', 20, 'PRune'],                       # primary rune
                ['pdodge', 200, 'SRune'],                   #secondary rune
                ['pdef%', 11, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['pdef%', 11, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['mdef%', 11, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['mdef%', 11, 'sub'], ['pdodge', 110, 'sub'], ['hp%', 11, 'sub'], ['pblock', 220, 'sub'], 
                ['hp', 870153, 'ring'],                   #accessory
                ['hp%', 30, 'perk'],                       #T1 perk
                ['FullGeneralUWRingMBL',0, 'name']
        ]
        heroes.append(createHero(FullGeneralUWRingMBL))
        '''
    return heroes

#module statDR
import math

def Attenuate(x,k,a,b):
    return math.floor(k * 1000000 / (a * x * x + b * x + 1000000));


def AttenuateInv(x,k,a,b):
    return k - math.floor(k * 1000000 / (a * x * x + b * x + 1000000));


#these return defense dmg reduction. To use, remember to use 1-mit for amount of passing dmg
def pdefMitigation(pdef):
    temp = 0.0

    # coefficients
    #a = 9.8422403011163961E-01
    #b = 9.6815105603447773E+03
    a= 0.9842
    b= 9681.5

    temp = (a * pdef) / (b + pdef)
    return temp

def mdefMitigation(mdef):
    temp = 0.0

    # coefficients
    #a = 9.8422403011163961E-01
    #b = 9.6815105603447773E+03
    a= 0.9842
    b= 9681.5

    temp = (a * mdef) / (b + mdef)
    return  temp

#testing:
#print 1- pdefMitigation(34235) #ok
#print 1- pdefMitigation(35235) #ok
#print 1- pdefMitigation(36235) #ok
#print 1- pdefMitigation(56235) #ok

def calcBlockChance(rawStat, frmt='d'):
    return calcBlockDodge(rawStat, frmt)

def calcDodgeChance(rawStat, frmt='d'):
    return calcBlockDodge(rawStat, frmt)


#function to calculate stat to efficiency gain for block and dodge (also lifesteal apperantly?)
#recieves rawStat and desired output format (p for percent, d for decimal)
#and returns gained effect (in decimal form by default)
#credit to Pearlite for formula
def calcBlockDodge(rawStat, frmt='d'):
    divisor = 1000
    if frmt == 'p':
        divisor = 10
    rawStat = rawStat*1.0 #just telling python to treat as float
    T1 = 500    #first soft cap
    T2 = 1000 #second soft cap
    if(rawStat > T2):      #third treshhold
        return AttenuateInv(rawStat, T2 , 3, 0)/divisor
    elif(T2 >= rawStat > T1):     #second treshhold
        return (math.floor(T1*rawStat/1000)+ 250)/divisor
    else:                    #first treshhold
        return rawStat/divisor

#testing values
#print calcBD(1500)
#print calcBD(1300)
#print calcBD(1000)
#print calcBD(750)
#print calcBD(500)
#print calcBD(300)
#print calcBD(0)


#My original
#def calcTough(t):
#    if t < 450:
#        return 1- t*1.0/1000
#    elif t > 450:
#        return  1- (0.45 + (t-450)*1.0/2500)
#    else :
#        return 0.65 #seems to be hard cap

#function to calculate mitigation for given toughness rating
#(apperantly also valid for penetration and cc resist)
#credit to Pearlite for formula
def calcTough(rawStat, frmt='d'):
    divisor = 1000
    if frmt == 'p':
        divisor = 10
    rawStat = rawStat*1.0 #just telling python to treat as float
    T1 = 450 #first soft cap
    T2 = 900 #second soft cap
    if rawStat > T2:
        return 1 - AttenuateInv(rawStat, T2 , 2, 1000)/divisor
    elif rawStat > T1:
        return 1 - (math.floor(409*rawStat/1000)+ 266)/divisor
    else:
        return 1- rawStat/divisor

#testing
#print calcTough(0)
#print calcTough(200)
#print calcTough(450)
#print calcTough(550) #should be 49%
#print calcTough(800)
#print calcTough(850)
#print calcTough(1000)
#seems legit


#function to calculate damage reduction by pblock def
#Probably falls off for high pblock def values (>400), but seems pretty accurate till then.
#recieves stat rate and returns decimal *total reduction*
def calcBlockDef(t):
    if t < 200:
        return 1 - (0.5 + t/1000)
    else:
        return 1 - (0.7 + (t-200.0)/3000)

#print calcBlockDef(0) #ok
#print calcBlockDef(200) #ok
#print calcBlockDef(300) #?
#print calcBlockDef(400) #?
#print calcBlockDef(600) #probably wrong, others pretty OK. noone runes 3 pbld anyways




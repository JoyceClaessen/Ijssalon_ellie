from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    return "vandaag in de aanbieding emmertje ijs (1 liter) in de smaak",smaak,"van", prijs,"euro voor", prijs-(prijs*korting),"euro."

print (aanbieding_1("aardbei",4,0.1))

inkomsten=[220,430,125,160,205,90,345]
def inkomsten_totaal(inkomsten):
    
    totaal= sum(inkomsten)
    btw= 0.09
    bedrag= totaal*btw
    return "Het totaal van alle inkomsten van deze week is",totaal,bedrag,"euro btw betaald dient te worden"
   
print (inkomsten_totaal(inkomsten))

mijn_lijst=[220,430,125,160,205,90,345]
def laag_en_hoog(mijn_lijst):
    return (max(mijn_lijst), min(mijn_lijst))

print (laag_en_hoog(mijn_lijst))

mijn_lijst=[220,430,125,160,205,90,345]
def gemiddelde(mijn_lijst):
    return (sum(mijn_lijst) / len(mijn_lijst))

print ("de gemiddelde inkomst van deze week zijn",gemiddelde(mijn_lijst),"euro.")

invoer_lijst=[10,5,3,2,1,2,9]
def meervoudig(invoer_lijst):
    return (laag_en_hoog(invoer_lijst))
    
print (meervoudig(invoer_lijst))

invoer_lijst_2= [1,2,3,4,5,6,7]
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

print(combinatie(invoer_lijst_2))
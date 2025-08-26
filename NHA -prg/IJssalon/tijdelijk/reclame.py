def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst

#les8 vraag5
def aanbieding_1(smaak, prijs, korting):
        prijs_na_korting = prijs * (1 - korting)
        uitvoer = f'''Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro.'''
        return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))


#les8 vraag6&7
def inkomsten_totaal(inkomsten):
        totaal = sum(inkomsten)
        bedrag = totaal * 0.09
        uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
        return uitvoer
        
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345]))

#les8 vraag8
def laag_en_hoog(mijn_lijst):
        laagste = min(mijn_lijst)
        hoogste = max(mijn_lijst)
        return [laagste, hoogste]
    
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

#les8 vraag9&10
def gemiddelde(mijn_lijst):
        bedrag = sum(mijn_lijst) // len(mijn_lijst)
        uitvoer = f"De gemiddelde inkomsten deze week zijn {bedrag} euro."
        return uitvoer

print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

#les8 vraag11
def meervoudig(invoer_lijst):
       return laag_en_hoog(invoer_lijst)
print(meervoudig([10,5,3,2,1,2,9]))

#les8 vraag12
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)  
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

print(combinatie([10,5,3,2,1,2,9]))


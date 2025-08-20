#les7 vraag2
prijzen = { 
    "aardbei": 3, 
    "vanille": 4, 
    "chocolade": 5 
} 

#les7 vraag3
aanbieding = prijzen["aardbei"] * 0.8 

#les7 vraag4
reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter – slechts € {aanbieding}"

#les7 vraag5
reclame_tekst2 = reclame_tekst[:63]
print(reclame_tekst2)

#les7 vraag6
reclame_tekst3=reclame_tekst2.upper()
print(reclame_tekst3)

#les7 vraag7
reclame_tekst4=reclame_tekst3.split()
print(reclame_tekst4)

#les7 vraag8
for el in reclame_tekst4:
    print(el)

#les7 vraag9
    print(el.lower())

#les7 vraag10
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())


from helper import som

#les10 vraag7&8
def presenteer(inkomsten_dict, totaal): 
    for item, bedrag in inkomsten_dict.items(): 
        print(f"{item}: {bedrag} euro")  
    print("==========================") 
    print(f"Totaal: {totaal} euro")  

mijn_dict = {
    "vis": 10, 
    "vlees": 25, 
    "overig": 15
}

totaal = som(mijn_dict)
presenteer(mijn_dict, totaal)
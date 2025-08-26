'''
def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

def fooi_pp(bedrag, personen):
    try:         bedrag_pp = bedrag/personen    
    except:         bedrag_pp = "??"    
    return f"Het bedrag per persoon is {bedrag_pp} euro"

b = int(input("Welk bedrag zit er in de fooienpot? "))
p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))
print(fooi_pp(b,p))
'''

#les10 vraag3
def som(inkomsten_dict): 
    totaal = 0 
    for item, bedrag in inkomsten_dict.items(): 
        totaal += bedrag  
    return totaal  

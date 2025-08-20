#les6 vraag 2a
mijn_dictionary = {  
    "Voornaam" : "Harry", 
    "Achternaam" : "van Winkel", 
    "Geboortedatum" : "27-03-1939",  
    }
print()
for k, v in mijn_dictionary.items():  
    print (k, v)


#les6 vraag 2b
mijn_dictionary = {  
    "Voornaam" : "Harry", 
    "Achternaam" : "van Winkel", 
    "Geboortedatum" : "27-03-1939",  
    }
print(mijn_dictionary["Voornaam"])

#les6 vraag 2c
mijn_dictionary = {  
    "Voornaam" : "Harry", 
    "Achternaam" : "van Winkel", 
    "Geboortedatum" : "27-03-1939",  
    }
mijn_dictionary.update({"Voornaam": "Henrikus"})
print()
for k, v in mijn_dictionary.items():  
    print (k, v)


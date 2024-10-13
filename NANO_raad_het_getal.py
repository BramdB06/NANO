#NANO app store
#Bram de Bondt
#V1D

def raad_het_getal():
    import random
    maximaal = int(input('Tot welk getal wil je raden? '))
    nummer = random.randrange(1, maximaal) #kiest random getal tussen 1 en maximaal wat de gebruiker kiest

    print(f'Ik heb een getal van 1 tot {maximaal} in mijn hoofd.')
    pogingen = int(input('Hoe vaak wil je raden? '))
    geradenGetallen = []

    for i in range(pogingen): #runt de code hieronder zovaak als de gebruiker hiervoor invulde
        gok = input(f'\nJe hebt nog {pogingen} poging(en).\n')

        while True:
            if not gok.isdigit() or int(gok) < 1 or int(gok) > maximaal: #checkt of de ingevoerde waarde een getal is en of het binnen de gekozen afstand zit
                print(f'Ongeldig, voer een getal tussen de 1 en {maximaal} in.')
                gok = input(f'\nJe hebt nog {pogingen} poging(en).\n')
            elif int(gok) in geradenGetallen: #checkt of het getal al eerder is geraden
                print('Dit getal heb je al geraden, voer een ander getal in.')
                gok = input(f'\nJe hebt nog {pogingen} poging(en).\n')
            else:
                gokGetal = int(gok) #maakt van de ingevoerde waarde een integer
                geradenGetallen.append(gokGetal) #voegt deze integer toe aan een list
                break

        if gokGetal == nummer: #als de gok gelijk is aan gekozen nummmer dan print de tekst hieronder en stopt de for loop
            print('Gefeliciteerd, je hebt het goed geraden!')
            break
        else: #als de gok niet gelijk is aan het gekozen nummer print tekst hieronder en gaat er een poging vanaf
            print('Helaas was dat niet het goede antwoord.')
            pogingen = pogingen - 1
        if pogingen == 0: #als de pogingen 0 nul zijn dan print dit hieronder en stopt de loop
            print(f'Het is je helaas niet gelukt om het getal te raden, het goede antwoord was {nummer}.')
def raad_het_getal():
    import random
    username = input('Hoe heet u? ')
    maximaal = int(input('Tot welk getal wil je raden? '))
    nummer = random.randrange(1, maximaal)
    afsluiting = 'Tot de volgende keer!'

    print(f'Oke {username}, ik heb een getal van 1 tot {maximaal} in mijn hoofd.')
    pogingen = int(input('Hoe vaak wil je raden? '))

    for i in range(pogingen):
        gok = int(input(f'\nJe hebt nog {pogingen} poging(en).\n'))
        pogingen = pogingen - 1

        if gok == nummer:
            print('Gefeliciteerd, je hebt het goed geraden!')
            print(afsluiting)
            break
        elif gok != nummer and pogingen == 0:
            print(f'Het is je helaas niet gelukt om het getal te raden, het goede antwoord was {nummer}.')
            print(afsluiting)
        else:
            print('Helaas was dat niet het goede antwoord.')
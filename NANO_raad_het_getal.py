def raad_het_getal():
    import random
    maximaal = int(input('Tot welk getal wil je raden? '))
    nummer = random.randrange(1, maximaal)

    print(f'Ik heb een getal van 1 tot {maximaal} in mijn hoofd.')
    pogingen = int(input('Hoe vaak wil je raden? '))

    for i in range(pogingen):
        gok = input(f'\nJe hebt nog {pogingen} poging(en).\n')
        try:
            if int(gok) == nummer:
                print('Gefeliciteerd, je hebt het goed geraden!')
                break
            elif int(gok) != nummer and pogingen == 0:
                print(f'Het is je helaas niet gelukt om het getal te raden, het goede antwoord was {nummer}.')
            else:
                print('Helaas was dat niet het goede antwoord.')
                pogingen = pogingen - 1
        except ValueError:
            print('Voer een getal in.')
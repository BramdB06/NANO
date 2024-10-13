#NANO app store
#Bram de Bondt
#V1D

def keuzemenu():
    from NANO_galgje import galgje #hier worden alle benodigde functies geimporteerd
    from NANO_raad_het_getal import raad_het_getal
    from NANO_shop_plaatje import NANO_titel

    print(f'{NANO_titel()}\n') #print de grote titel
    naam = input('Hoe heet u? ') #vraagt om de naam van de gebruiker

    print(f'''\nHallo {naam}, welkom bij Brams Boetiek!
Zin om je te vermaken? Wij hebben hier twee spellentjes waar je uit kan kiezen:

    1. Raad het getal
    2. Galgje''')

    doorspelen = '\nWil je doorspelen? ja/nee : '
    spelen = input('\nWil je een spelletje spelen? ja/nee : ').lower() #vraagt of gebruiker wil spelen

    while True:
        if spelen == 'ja': #checkt of gebruiker ja heeft geantwoord en runt de code hieronder.
            keuze = input('Welke wil je spelen? 1/2 : ') #vraagt welk spel de gebruiker wil spelen
            try:
                if int(keuze) == 1: #als 1 is getypt dan wordt raad het getal gerund
                    print()
                    raad_het_getal()
                    spelen = input(doorspelen).lower() #vraagt of gebruiker door wil spelen en verandert de waarde van 'spelen'
                elif int(keuze) == 2: #als 2 is getypt dan wordt galgje gerund
                    print()
                    galgje()
                    spelen = input(doorspelen).lower() #vraagt of gebruiker door wil spelen en verandert de waarde van 'spelen'
                else:
                    print('Ongeldige keuze, kies 1 voor raad het getal of 2 voor galgje.') #als anders getal dan 1 of 2 is gegeven dan print dit
            except ValueError:
                print('Er is iets fout gegaan, vul de volgende keer een getal in.') #als er een string is gegeven print dit
        elif spelen == 'nee': #als gebruiker nee invoert print de code hieronder en stopt de while loop
            print('Oke, bedankt voor het spelen en tot ziens!')
            break
        else:
            print('Je moet antwoord geven met ja of nee.') #als gebruiker iets anders invoert dan ja of nee print dit.
            spelen = input(doorspelen).lower() #vraagt of gebruiker door wil spelen en verandert de waarde van 'spelen'


keuzemenu()
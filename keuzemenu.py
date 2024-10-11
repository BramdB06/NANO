def keuzemenu():
    from NANO_galgje import galgje
    from NANO_raad_het_getal import raad_het_getal
    from NANO_shop_plaatje import NANO_titel

    print(f'{NANO_titel()}\n')
    naam = input('Hoe heet u? ')

    print(f'''\nHallo {naam}, welkom bij Brams Boetiek!
Zin om je te vermaken? Wij hebben hier twee spellentjes waar je uit kan kiezen:

    1. Raad het getal
    2. Galgje''')

    doorspelen = '\nWil je doorspelen? ja/nee : '
    spelen = input('\nWil je een spelletje spelen? ja/nee : ')

    while True:
        if spelen == 'ja':
            keuze = input('Welke wil je spelen? 1/2 : ')
            try:
                if int(keuze) == 1:
                    print()
                    raad_het_getal()
                    spelen = input(doorspelen)
                elif int(keuze) == 2:
                    print()
                    galgje()
                    spelen = input(doorspelen)
                else:
                    print('Ongeldige keuze, kies 1 voor raad het getal of 2 voor galgje.')
            except ValueError:
                print('Er is iets fout gegaan, vul de volgende keer een getal in.')
        elif spelen == 'nee':
            print('Oke, bedankt voor het spelen en tot ziens!')
            break
        else:
            print('Je moet antwoord geven met ja of nee.')
            spelen = input(doorspelen)


keuzemenu()
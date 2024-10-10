from NANO_galgje import galgje
from NANO_raad_het_getal import raad_het_getal

print('''Welkom bij Brams Boetiek!
Dit is DE plek om je te vermaken, wij hebben twee spellentjes waar je uit kan kiezen:
1. Raad het getal
2. Galgje
''')

while True:
    doorspelen = input('Wil je een spelletje spelen? ja/nee').lower()
    if doorspelen == 'ja':
        keuze = input('Welke wil je spelen? 1/2')
        if keuze == 1:
            raad_het_getal()
        elif keuze == 2:
            galgje()
        else:
            print('ongeldig, voor raad het getal moet je 1 invoeren en voor galgje moet je 2 invoeren')
    elif doorspelen == 'nee':
        print('Oke, bedankt voor het spelen en tot ziens!')
        break
    else:
        print('Je moet antwoord geven met ja of nee.')
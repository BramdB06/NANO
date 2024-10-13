#NANO app store
#Bram de Bondt
#V1D

def galgje():
    import random #importeert alle benodigde functies en modules
    from Galgje_plaatjes import plaatje_print

    with open('Galgje_bestand.txt', 'r') as woorden:
        woordenlijst = [line.strip() for line in woorden.readlines()] #stript alle regels in het txt bestand en maakt een lijst van alle woorden
    woord = random.choice(woordenlijst) #kiest willekeurig woord uit een txt file

    print(f'Ik heb een woord van {len(woord)} letters uitgekozen voor galgje.')

    verstopt_woord = ['_' for _ in woord] # maakt een lijst met een '_' voor elke letter in het gekozen woord

    aantal_fouten = 0
    verkeerde_letters = []
    geraden_letters = []

    def raden():
        nonlocal aantal_fouten #laat de variabele aantal_fouten uit de omliggende functie gewijzigd worden

        print(f'\n{"".join(verstopt_woord)}')
        poging = input('Geef een letter of het hele woord als je het antwoord al weet: ').lower() #maakt van de input allemaal kleine letters

        if poging.isdigit(): #als de ingevulde gok een cijfer is print dit
            print('Sorry, ik accepteer geen getal als poging.')

        elif poging == '' or poging == ' ': #als de ingevulde poging leeg is of alleen een spatie bevat print dit
            print('Vul iets in.')

        elif poging in geraden_letters: #als de ingevulde poging gelijk is aan iets wat al eerder is geraden print dit
            print('Dit heb je al geraden!')

        elif poging not in woord: #als de geraden letter niet in het woord zit dan print het plaatje en de letters die verkeerd waren.
            if len(poging) > 1: #als de gebruiker meer dan 1 letter invoert ziet het programma het al woord en print het volgende
                geraden_letters.append(poging)
                verkeerde_letters.append(poging)
                print(f'''{poging} is niet het goede antwoord.
{plaatje_print(aantal_fouten)}
    Verkeerde letters of woorden: {', '.join(verkeerde_letters)}''')
                aantal_fouten += 1 #het aantal fouten wordt verhoogd, deze variabele wordt gebruikt om het goede plaatje te printen

            else: #als het maar 1 letter is komt die letter in de lijst met geraden letters en met verkeerde letters gestopt
                geraden_letters.append(poging)
                verkeerde_letters.append(poging)
                print(f'''{poging} zit helaas niet in het woord.
{plaatje_print(aantal_fouten)}
    Verkeerde letters of woorden: {', '.join(verkeerde_letters)}''')
                aantal_fouten += 1

            if aantal_fouten == 7: #als het aantal fouten 7 is print het volgende en returnt er 1, dit stopt de code
                print(f'\nHet is je helaas niet gelukt om het woord te raden, het goede antwoord was {woord}.')
                return 1

        elif poging == woord: #als de gebruiker een woord invult die gelijk is aan het gekozen woord dan print dit en return er 1 dus dan stopt de code
            print(f'\nJe hebt het woord goed geraden, gefeliciteerd!')
            return 1

        else: #als de letter in het woord zit gebeurt het volgende
            geraden_letters.append(poging)
            for index, letter in enumerate(woord): #geeft voor elke letter in het woord zowel de index als de bijbehorende letter
                if letter == poging: #als de geraden letter gelijk is aan de letter op een bepaalde plek in het woordt dan verandert de '_' met die letter
                    verstopt_woord[index] = poging
            if '_' not in verstopt_woord: #als er een '_' meer inzitten dan print dit en returnt er weer 1 dus dan stopt de code
                print(f'\nJe hebt de laatste letter geraden!, gefeliciteerd! Het woord was dus {woord}.')
                return 1

    while True:
        if raden() == 1: #runt de functie totdat de returnwaarde 1 is, als dat zo is volgt een break
            break
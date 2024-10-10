def galgje():
    import random
    from Galgje_plaatjes import plaatje_print

    with open('Galgje_bestand.txt', 'r') as woorden:
        woordenlijst = [line.strip() for line in woorden.readlines()]
    woord = random.choice(woordenlijst)

    print(f'Ik heb een woord van {len(woord)} letters uitgekozen voor galgje.')

    verstopt_woord = ['_' for _ in woord]
    afsluiting = 'Tot de volgende keer!'

    aantal_fouten = 0
    verkeerde_letters = []
    geraden_letters = []

    def raden():
        nonlocal aantal_fouten
        print(f'\n{"".join(verstopt_woord)}')
        poging = input('Geef een letter of het hele woord als je het antwoord al weet: ').lower()
        if poging in geraden_letters:
            print('Deze letter is al geraden!')
        elif poging not in woord:
            if len(poging) > 1:
                print(f'''{poging} is niet het goede antwoord
{plaatje_print(aantal_fouten)}''')
                aantal_fouten += 1
            else:
                geraden_letters.append(poging)
                verkeerde_letters.append(poging)
                print(f'''{poging} zit helaas niet in het woord.
{plaatje_print(aantal_fouten)}
        Al geraden letters: {' '.join(verkeerde_letters)}''')
                aantal_fouten += 1
            if aantal_fouten == 7:
                print(f'''\nHet is je helaas niet gelukt om het woord te raden, het goede antwoord was {woord}.
{afsluiting}''')
                return 1
        elif poging == woord:
            print(f'\nJe hebt het goede woord geraden, gefeliciteerd!')
            return 1
        else:
            geraden_letters.append(poging)
            for index, letter in enumerate(woord):
                if letter == poging:
                    verstopt_woord[index] = poging
            if '_' not in verstopt_woord:
                print(f'\nJe hebt de laatste letter geraden!, gefeliciteerd! Het woord was dus {woord}.!')
                return 1

    while True:
        if raden() == 1:
            break
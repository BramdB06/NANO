import random
username = input('Hoe heet u?\n')
maximaal = int(input('Tot welk getal wilt u raden?\n'))
number = random.randrange(1, maximaal)
win = 'U heeft het goed geraden, gefeliciteerd en tot ziens!'
verkeerdePoging = 'Helaas was dat niet het goede antwoord.'
verlies = 'Het is u helaas niet gelukt om het getal te raden.'
afsluiting = 'Tot de volgende keer!'
pogingen = int(input('Hoe vaak wilt u raden?\n'))

print('Hallo ' + username + ', ik heb een getal van 1 tot ' + str(maximaal) + ' in mijn hoofd.')

for i in range(pogingen):
    guess = int(input('U heeft nog ' + str(pogingen) + ' poging(en).\n'))
    pogingen = pogingen - 1

    if guess == number:
        print(win)
        print(afsluiting)
        break
    elif guess != number and pogingen == 0:
        print(verlies)
        print(afsluiting)
    else:
        print(verkeerdePoging)
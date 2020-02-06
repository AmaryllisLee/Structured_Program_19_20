import random
'''
Schrijf een programma dat een willekeurige getal kiest en de
gebruiker net zo lang laat gokken tot dat ze het goed hebben
'''
def guess():
    nummer = random.randrange(1, 100)
    print(nummer)
    while True:
        n = int(input('Guess a number between 1 and 100: '))
        if n != nummer:
            continue
        else: # n==nummer => Gebruiker heeft het nummer correct gegokt.
            return 'You guessd correctly'
            break

#Controle
print(guess())
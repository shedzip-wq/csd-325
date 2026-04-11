# Sheridan Dela Cruz
# April 11, 2026
# Module 3.2

# Modified version of Al Sweigart's Cho-Han game.

# CHANGES MADE FOR ASSIGNMENT:
# 1. Updated all input prompts to use my initials "SDC:" instead of ">".
# 2. Changed the house fee from 10% to 12%.
# 3. Added a notice in the introduction about a bonus rule:
#       - If the dice total is 2 or 7, the player receives a 10-month bonus.
# 4. Implemented the bonus rule in the game logic:
#       - When total == 2 or total == 7, display a message and add +10 to purse.

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, Modified Version

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS RULE: If the dice total is 2 or 7, you receive a 10-month bonus!
''')

purse = 5000

while True:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    
    # Ask for bet
    while True:
        pot = input('SDC: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.\n')
    print('    CHO (even) or HAN (odd)?')

    # Player chooses CHO or HAN
    while True:
        bet = input('SDC: ').upper()
        if bet not in ('CHO', 'HAN'):
            print('Please enter either "CHO" or "HAN".')
        else:
            break

    # Reveal dice
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Bonus rule
    if total == 2 or total == 7:
        print(f'BONUS! The total was {total}. You receive a 10-month bonus!')
        purse += 10

    # Determine correct bet
    correctBet = 'CHO' if total % 2 == 0 else 'HAN'
    playerWon = (bet == correctBet)

    # Apply win/loss
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot
        houseFee = int(pot * 0.12)  # 12% house fee
        print('The house collects a', houseFee, 'mon fee.')
        purse -= houseFee
    else:
        purse -= pot
        print('You lost!')

    # Check purse
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()

import random,time
name = input('\nEnter your name: ')
if not name:
    pass
print("\n\t\tWelcome to the game....\n\n You need to guess number between 1 to 50\n")
random_number = random.randint(1,50)
guess_chance = 0
while True:
    guess_chance+=1
    try:
        entered_number  = int(input('\nEnter the number: '))
    except:
        print('\nOnly integers are allowed\n')
        continue
    if random_number==entered_number:
        print(f'\nYou guess correct in {guess_chance} chances \n')
        guess_chance=0
        play_again = input('\nDo you want to play again y/n? ')
        if play_again.lower()=='y':
            random_number = random.randint(1,50)
            continue
        print(f'\nThanks  {name}  for playing!!!\n')
        time.sleep(5)
        exit()
    if random_number>entered_number:
        print('\nToo low\n\nGuess again\n')
    if random_number<entered_number:
        print('\nToo high\n\nGuess again\n')
    continue
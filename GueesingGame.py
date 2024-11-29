import random
def guessing_game():
    print("Welcome to the guessing game")
    attempts=0
    secret_number=random.randint(0,50)
    
    while True:
        try:
            attempts+=1
            Guess=int(input('Insert any number between 0 and 50: '))
            if secret_number<Guess:
                            print('Guess too high')
            elif secret_number>Guess:
                            print('Guess too low')
            else:
                    print(f'Congradulations! you have guessed the correct number in {attempts} attempts')
                    break
    
        except ValueError:
                        print('Invalid input')
    
guessing_game()

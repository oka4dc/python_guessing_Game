import random
#random_num = random.randint(2,5)
#rand_number = random.randrange(1,10)
#print(random_num)
#print(rand_number)

def guess(a):
    guess_number = random.randint(1, a)
    print(guess_number)
    guess =0
    chances = 3
    while  chances<=3:
        
        if guess != guess_number:
            guess = int(input(f"please enter a number between 1 and {a}: "))
            if guess> guess_number:
                print ('sorry the number you entered is greater ')
            elif guess < guess_number:
                print('sorry the number you entered is less ')
            else:
                print('congratulations!.....you just guessed d right number')
        chances = chances +1
    else:
        print ('sorry you lost')
    
        
guess(10)

print ('welcome')
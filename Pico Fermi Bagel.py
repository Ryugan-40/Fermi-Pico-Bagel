import random
num=input('Enter the number of digits ')
original_number=str(int(random.random()*(10**int(num))))

while True:
    output=[]
    guess_number=input('\nGuess the number: ')
    
    if len(guess_number) != len(original_number):
        print(f'Enter {len(original_number)} digit number')
        continue
    if len(guess_number) != len(set(guess_number)):
        print('Duplicate Number')
        continue
    if (int(guess_number)-int(original_number)) == 0:
        print('Fermi '*len(str(original_number)))
        print('\nYou Won !!')
        break
    
    for i in range(len(original_number)):
        for j in range(len(guess_number)):
            if original_number[i] == guess_number[j]:
                if i == j:
                    output.append('Fermi')
                else:
                    output.append('Pico')
    
    output_string = ' '.join(output)
        
    if len(output)==0:
        print('Bagels')
    else:
        print(output_string)
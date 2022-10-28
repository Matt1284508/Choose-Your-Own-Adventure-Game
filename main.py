print('''
0================================================0
|'.                    (|)                     .'|
|  '.                   |                    .'  |
|    '.                |O|                 .'    |
|      '. ____________/===\_____________ .'      |
|        :            `\"/`  ______     :     .. |
|        :     mmmmmmm  V   |--%%--|    :   .'|| |
|        :     |  |  |      |-%%%%-|    :  |  || |
|        :     |--|--| @@@  |=_||_=|    :  I  || |
|        :     |__|__|@@@@@ |_\__/_|    :  |  || |
|        :             \|/   ____       :  |  || |
|        :;;       .'``(_)```\__/````:  :  |  || |
|        :||___   :================:'|  :  | 0+| |
|        :||===)  | |              | |  :  |  || |
|        ://``\\__|_|______________|_|__:  I  || |
|      .'/'    \' | '              | '   '.|  || |
|    .'           |                |       '. || |
|  .'                                        '|| |
|.' Spicer                                     '.|
0================================================0
''')
print('Welcome to the escape room!')
print('Your goal is to make it out alive.')

# Level One
level_one_choice = input('Do you enter Door 1 or Door 2 \n Door:')
if level_one_choice == '2':
# Level Two
    level_two_choice = input('Which rope do you pull? Red or Black \n')
    level_two_lower = level_two_choice.lower()
    if level_two_lower == 'red':
# Level Three        
        level_three_choice  = input('Two secret passages open. Left or right? \n')
        level_three_lower = level_three_choice.lower()
        if level_three_lower == 'left':
            print('Congratulations, you escaped!')
        elif level_three_lower == 'right':
            print('Eaten by beasts. Game Over!')
        else: 
            print('Game Over!')
    else: 
        print('A trap door opens and you fall to your death. Game over!')
else:
    print('You enter a pitch black room and the door locks behind you. You cannot escape. Game over!')




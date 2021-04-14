from os import system


x_input = '  X '
o_input = '  O '
space = '    '
wall = '|'
floor = '----'
x_place = []
o_place = []
horizontal = [[1,2,3], [4,5,6], [7,8,9]]
vertical = [[1,4,7], [2,5,8], [3,6,9]]
diagonal = [[1,5,9], [3,5,7]]
game_over = [i for i in horizontal] + [i for i in vertical] + [i for i in diagonal]



def initial_walls():
    for i in range(3):
        print(space+wall+space+wall+space)
        if i < 2:
            print(floor+'-'+ floor+'-'+ floor)

def put_X_at(coord):
    for curr in reversed(range(1, 10)):
        if coord == curr:
            print(x_input, end='')
        else:
            if curr in x_place:
                print(x_input, end='')
            elif curr in o_place:
                print(o_input, end='')
            else:
                print(space, end='')

        if curr in [4, 7]:
            print('\n' + floor + '-' + floor + '-' + floor)
        else:
            if curr != 1:
                print(wall, end='')

def put_O_at(coord):
    for curr in reversed(range(1, 10)):
        if coord == curr:
            print(o_input, end='')
        else:
            if curr in x_place:
                print(x_input, end='')
            elif curr in o_place:
                print(o_input, end='')
            else:
                print(space, end='')

        if curr in [4, 7]:
            print('\n' + floor + '-' + floor + '-' + floor)
        else:
            if curr != 1:
                print(wall, end='')

def game_checker():
    x_set, o_set = set(x_place), set(o_place)
    for win in game_over:
        if set(win).intersection(x_set) == set(win):
            print('\nX WINS!')
            return True
        elif set(win).intersection(o_set) == set(win):
            print('\nO WINS!')
            return True
    return False

def x_play():
    x = 10
    while True:
        while x < 1 or x > 9:
            try:
                x = int(input('\nPlace X at: '))
                if x in x_place or x in o_place:
                    raise Exception('x is already occupied')
            except ValueError:
                print('Invalid Input')
                x = int(input('\nPlace X at: '))
            except Exception:
                print("There's already someone there")
                x = int(input('\nPlace X at: '))
            if x < 1 or x > 9:
                print('Value out of range')


        if x not in x_place and x not in o_place:
            put_X_at(x)
            x_place.append(x)
            break


def o_play():
    o = 10
    while True:
        while o < 1 or o > 9:
            try:
                o = int(input('\nPlace O at: '))
                if o in x_place or o in o_place:
                    raise Exception('o is already occupied')
            except ValueError:
                print('Invalid Input')
                o = int(input('\nPlace O at: '))
            except Exception:
                print("There's already someone there")
                o = int(input('\nPlace O at: '))
            if o < 1 or o > 9:
                print('Value out of range')

        if o not in x_place and o not in o_place:
            put_O_at(o)
            o_place.append(o)
            break

        else:
            print("There's already someone there")
            put_X_at(0)


choice = input('Do you want to play?(Y/N)')
while choice.upper() != 'N':
    x_place.clear()
    o_place.clear()
    player1_choice = input('X or O?\nPlayer 1: ')
    put_X_at(0)

    if player1_choice.upper() == 'X':
        for i in range(5):
            x_play()
            if game_checker():
                break

            if i < 4:
                o_play()
            if game_checker():
                break

    elif player1_choice.upper() == 'O':
        for i in range(5):
            o_play()
            if game_checker():
                break

            if i < 4:
                x_play()
            if game_checker():
                break

    choice = input('\nDo you want to play again?(Y/N)')
    system('cls')
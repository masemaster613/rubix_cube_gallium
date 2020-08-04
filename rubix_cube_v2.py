#imports
import copy
import random

#set up cube
face0 = [['r', 'r'], ['r', 'r']]
face1 = [['b', 'b'], ['b', 'b']]
face2 = [['o', 'o'], ['o', 'o']]
face3 = [['g', 'g'], ['g', 'g']]
face4 = [['y', 'y'], ['y', 'y']]
face5 = [['w', 'w'], ['w', 'w']]
my_cube = [face0, face1, face2, face3, face4, face5]
#show the cube
def print_cube(cube):
    row1 = cube[4][0] + cube[0][0] + cube[5][0]
    row2 = cube[4][1] + cube[0][1] + cube[5][1]
    print(" ".join(row1))
    print(" ".join(row2))
    for row in cube[1] + cube[2] + cube[3]:
        print(" " * 4, end = "")
        print(" ".join(row))
#make a general move thing
def move(cube, dic):
    old_cube = copy.deepcopy(cube)
    new_cube = copy.deepcopy(cube)
    for i in dic:
        old_pos = i.split(' ')
        new_pos = dic[i].split(' ')
        new_cube[int(new_pos[0])][int(new_pos[1])][int(new_pos[2])] = old_cube[int(old_pos[0])][int(old_pos[1])][int(old_pos[2])]
    return new_cube

#set up dictionaries for each move

row0_right = {'4 0 0':'0 0 0', '4 0 1':'0 0 1',
              '0 0 0':'5 0 0', '0 0 1':'5 0 1',
              '5 0 0':'2 1 0', '5 0 1':'2 1 1',
              '2 1 0':'4 0 0', '2 1 1':'4 0 1',
              '3 0 1':'3 0 0', '3 1 1':'3 0 1',
              '3 0 0':'3 1 0', '3 1 0':'3 1 1'}
row0_left =  {'5 0 0':'0 0 0', '5 0 1':'0 0 1',
              '2 1 0':'5 0 0', '2 1 1':'5 0 1',
              '4 0 0':'2 1 0', '4 0 1':'2 1 1',
              '0 0 0':'4 0 0', '0 0 1':'4 0 1',
              '3 1 0':'3 0 0', '3 0 0':'3 0 1',
              '3 1 1':'3 1 0', '3 0 1':'3 1 1'}
row1_right = {'4 1 0':'0 1 0', '4 1 1':'0 1 1',
              '0 1 0':'5 1 0', '0 1 1':'5 1 1',
              '5 1 0':'2 0 0', '5 1 1':'2 0 1',
              '2 0 0':'4 1 0', '2 0 1':'4 1 1',
              '1 1 0':'1 0 0', '1 0 0':'1 0 1',
              '1 1 1':'1 1 0', '1 0 1':'1 1 1'}
row1_left =  {'5 1 0':'0 1 0', '5 1 1':'0 1 1',
              '2 0 0':'5 1 0', '2 0 1':'5 1 1',
              '4 1 0':'2 0 0', '4 1 1':'2 0 1',
              '0 1 0':'4 1 0', '0 1 1':'4 1 1',
              '1 0 1':'1 0 0', '1 1 1':'1 0 1',
              '1 0 0':'1 1 0', '1 1 0':'1 1 1'}



col0_up   =  {'1 0 0':'0 0 0', '1 1 0':'0 1 0',
              '2 0 0':'1 0 0', '2 1 0':'1 1 0',
              '3 0 0':'2 0 0', '3 1 0':'2 1 0',
              '0 0 0':'3 0 0', '0 1 0':'3 1 0',
              '4 0 1':'4 0 0', '4 1 1':'4 0 1',
              '4 0 0':'4 1 0', '4 1 0':'4 1 1',}

col0_down =  {'3 0 0':'0 0 0', '3 1 0':'0 1 0',
              '0 0 0':'1 0 0', '0 1 0':'1 1 0',
              '1 0 0':'2 0 0', '1 1 0':'2 1 0',
              '2 0 0':'3 0 0', '2 1 0':'3 1 0',
              '4 1 0':'4 0 0', '4 0 0':'4 0 1',
              '4 1 1':'4 1 0', '4 0 1':'4 1 1',}

col1_up   =  {'1 0 1':'0 0 1', '1 1 1':'0 1 1',
              '2 0 1':'1 0 1', '2 1 1':'1 1 1',
              '3 0 1':'2 0 1', '3 1 1':'2 1 1',
              '0 0 1':'3 0 1', '0 1 1':'3 1 1',
              '5 1 0':'5 0 0', '5 0 0':'5 0 1',
              '5 1 1':'5 1 0', '5 0 1':'5 1 1',}

col1_down =  {'3 0 1':'0 0 1', '3 1 1':'0 1 1',
              '0 0 1':'1 0 1', '0 1 1':'1 1 1',
              '1 0 1':'2 0 1', '1 1 1':'2 1 1',
              '2 0 1':'3 0 1', '2 1 1':'3 1 1',
              '5 0 1':'5 0 0', '5 1 1':'5 0 1',
              '5 0 0':'5 1 0', '5 1 0':'5 1 1',}



top_c     =  {'5 1 0':'1 0 0', '5 0 0':'1 0 1',
              '1 0 0':'4 0 1', '1 0 1':'4 1 1',
              '4 1 1':'3 1 0', '4 0 1':'3 1 1',
              '3 1 0':'5 0 0', '3 1 1':'5 1 0',
              '0 1 0':'0 0 0', '0 0 0':'0 0 1',
              '0 1 1':'0 1 0', '0 0 1':'0 1 1'}

top_cc    =  {'4 0 1':'1 0 0', '4 1 1':'1 0 1',
              '3 1 0':'4 0 1', '3 1 1':'4 1 1',
              '5 1 0':'3 1 0', '5 0 0':'3 1 1',
              '1 0 0':'5 0 0', '1 0 1':'5 1 0',
              '0 0 1':'0 0 0', '0 1 1':'0 0 1',
              '0 0 0':'0 1 0', '0 1 0':'0 1 1'}

bottom_c  =  {'5 1 1':'1 1 0', '5 0 1':'1 1 1',
              '1 1 0':'4 0 0', '1 1 1':'4 1 0',
              '4 0 0':'3 0 0', '4 1 0':'3 0 1',
              '3 0 0':'5 0 1', '3 0 1':'5 1 1',
              '2 0 1':'2 0 0', '2 1 1':'2 0 1',
              '2 0 0':'2 1 0', '2 1 0':'2 1 1'}

bottom_cc =  {'4 0 0':'1 1 0', '4 1 0':'1 1 1',
              '3 0 1':'4 0 0', '3 0 0':'4 1 0',
              '5 0 1':'3 0 0', '5 1 1':'3 0 1',
              '1 1 1':'5 0 1', '1 1 0':'5 1 1',
              '2 1 0':'2 0 0', '2 0 0':'2 0 1',
              '2 1 1':'2 1 0', '2 0 1':'2 1 1'}

moves = [row0_right, row0_left, row1_right, row1_left, col0_up, col0_down, col1_up, col1_down, top_c, top_cc, bottom_c, bottom_cc]
#randomize cube
def randomize_cube(cube):
    random_cube = copy.deepcopy(cube)
    for z in range(random.randint(5,15)):
        for i in range(len(moves)):
            for x in range(random.randint(1,4)):
                random_cube = move(random_cube, moves[i])
    return random_cube

#ask for moves
print_cube(my_cube)
while True:
    which = input('row, column or spin? ')
    if which == 'row':
        row_num = input('which row (0/1)? ')
        l_r = input('left or right (l/r)? ')
        if row_num == '0':
            if l_r == 'r':
                my_cube = move(my_cube, row0_right)
            elif l_r == 'l':
                my_cube = move(my_cube, row0_left)
            else:
                print('error')
        elif row_num == '1':
            if l_r == 'r':
                my_cube = move(my_cube, row1_right)
            elif l_r == 'l':
                my_cube = move(my_cube, row1_left)
            else:
                print('error')
        else:
            print('error')
    elif which == 'column':
        col_num = input('which column (0/1)? ')
        u_d = input('up or down (u/d)? ')
        if col_num == '0':
            if u_d == 'u':
                my_cube = move(my_cube, col0_up)
            elif u_d == 'd':
                my_cube = move(my_cube, col0_down)
            else:
                print('error')
        elif col_num == '1':
            if u_d == 'u':
                my_cube = move(my_cube, col1_up)
            elif u_d == 'd':
                my_cube = move(my_cube, col1_down)
            else:
                print('error')
        else:
            print('error')
    elif which == 'spin':
        t_b = input('top or bottom (t/b)? ')
        direction = input('which way (c/cc)? ')
        if t_b == 't':
            if direction == 'c':
                my_cube = move(my_cube, top_c)
            elif direction == 'cc':
                my_cube = move(my_cube, top_cc)
            else:
                print('error')
        elif t_b == 'b':
            if direction == 'c':
                my_cube = move(my_cube, bottom_c)
            elif direction == 'cc':
                my_cube = move(my_cube, bottom_cc)
            else:
                print('error')
        else:
            print('error')
    elif which == 'random':
        my_cube = randomize_cube(my_cube)
    elif which == 'exit':
        break
    else:
        print('error')
    print_cube(my_cube)



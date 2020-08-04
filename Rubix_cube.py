#imports

#set up cube
face0 = [['r', 'r'], ['r', 'r']]
face1 = [['b', 'b'], ['b', 'b']]
face2 = [['o', 'o'], ['o', 'o']]
face3 = [['g', 'g'], ['g', 'g']]
face4 = [['y', 'y'], ['y', 'y']]
face5 = [['w', 'w'], ['w', 'w']]
cube = [face0, face1, face2, face3, face4, face5]
#show the cube
def print_cube():
    global cube
    row1 = cube[4][0] + cube[0][0] + cube[5][0]
    row2 = cube[4][1] + cube[0][1] + cube[5][1]
    print(" ".join(row1))
    print(" ".join(row2))
    for row in cube[1] + cube[2] + cube[3]:
        print(" " * 4, end = "")
        print(" ".join(row))
        
#set up 12 possible moves
def row0_right():
    global cube
    f0r0 = cube[4][0]
    f5r0 = cube[0][0]
    f2r1 = cube[5][0]
    f4r0 = cube[2][1]
    f3r0 = []
    f3r1 = []
    f3r0.append(cube[3][0][1])
    f3r0.append(cube[3][1][1])
    f3r1.append(cube[3][0][0])
    f3r1.append(cube[3][1][0])
    cube[0][0] = f0r0
    cube[5][0] = f5r0
    cube[2][1] = f2r1
    cube[4][0] = f4r0
    cube[3][0] = f3r0
    cube[3][1] = f3r1

def row0_left():
    global cube
    f0r0 = cube[5][0]
    f5r0 = cube[2][1]
    f2r1 = cube[4][0]
    f4r0 = cube[0][0]
    f3r0 = []
    f3r1 = []
    f3r0.append(cube[3][1][0])
    f3r0.append(cube[3][0][0])
    f3r1.append(cube[3][1][1])
    f3r1.append(cube[3][0][1])
    cube[0][0] = f0r0
    cube[5][0] = f5r0
    cube[2][1] = f2r1
    cube[4][0] = f4r0
    cube[3][0] = f3r0
    cube[3][1] = f3r1

def row1_right():
    global cube
    f0r1 = cube[4][1]
    f5r1 = cube[0][1]
    f2r0 = cube[5][1]
    f4r1 = cube[2][0]
    f1r0 = []
    f1r1 = []
    f1r0.append(cube[1][0][1])
    f1r0.append(cube[1][1][1])
    f1r1.append(cube[1][0][0])
    f1r1.append(cube[1][1][0])
    cube[0][1] = f0r1
    cube[5][1] = f5r1
    cube[2][0] = f2r0
    cube[4][1] = f4r1
    cube[1][0] = f1r1
    cube[1][1] = f1r1

def row1_left():
    global cube
    f0r1 = cube[5][1]
    f5r1 = cube[2][0]
    f2r0 = cube[4][1]
    f4r1 = cube[0][1]
    f1r0 = []
    f1r1 = []
    f1r0.append(cube[1][1][1])
    f1r0.append(cube[1][0][1])
    f1r1.append(cube[1][1][0])
    f1r1.append(cube[1][0][0])
    cube[0][1] = f0r1
    cube[5][1] = f5r1
    cube[2][0] = f2r0
    cube[4][1] = f4r1
    cube[1][0] = f1r0
    cube[1][1] = f1r1

def col0_up():
    global cube
    f0c0 = [cube[1][0][0], cube[1][1][0]]
    f1c0 = [cube[2][0][0], cube[2][1][0]]
    f2c0 = [cube[3][0][0], cube[3][1][0]]
    f3c0 = [cube[0][0][0], cube[0][1][0]]
    f4r0 = []
    f4r1 = []
    f4r0.append(cube[4][0][1])
    f4r0.append(cube[4][1][1])
    f4r1.append(cube[4][0][0])
    f4r1.append(cube[4][1][0])
    columns = {0:f0c0 , 1:f1c0 , 2:f2c0, 3:f3c0}
    for face in columns:
        cube[face][0][0] = columns[face][0]
        cube[face][1][0] = columns[face][1]
    cube[4][0] = f4r0
    cube[4][1] = f4r1

def col1_up():
    global cube
    f0c1 = [cube[1][0][1], cube[1][1][1]]
    f1c1 = [cube[2][0][1], cube[2][1][1]]
    f2c1 = [cube[3][0][1], cube[3][1][1]]
    f3c1 = [cube[0][0][1], cube[0][1][1]]
    f5r0 = []
    f5r1 = []
    f5r0.append(cube[5][0][1])
    f5r0.append(cube[5][1][1])
    f5r1.append(cube[5][0][0])
    f5r1.append(cube[5][1][0])
    columns = {0:f0c1 , 1:f1c1 , 2:f2c1, 3:f3c1}
    for face in columns:
        cube[face][0][1] = columns[face][0]
        cube[face][1][1] = columns[face][1]
    cube[5][0] = f5r0
    cube[5][1] = f5r1

def col0_down():
    global cube
    f0c0 = [cube[3][0][0], cube[3][1][0]]
    f1c0 = [cube[0][0][0], cube[0][1][0]]
    f2c0 = [cube[1][0][0], cube[1][1][0]]
    f3c0 = [cube[2][0][0], cube[2][1][0]]
    f4r0 = []
    f4r1 = []
    f4r0.append(cube[4][1][0])
    f4r0.append(cube[4][0][0])
    f4r1.append(cube[4][1][1])
    f4r1.append(cube[4][0][1])
    columns = {0:f0c0 , 1:f1c0 , 2:f2c0, 3:f3c0}
    for face in columns:
        cube[face][0][0] = columns[face][0]
        cube[face][1][0] = columns[face][1]
    cube[4][0] = f4r0
    cube[4][1] = f4r1

def col1_down():
    global cube
    f0c1 = [cube[3][0][1], cube[3][1][1]]
    f1c1 = [cube[0][0][1], cube[0][1][1]]
    f2c1 = [cube[1][0][1], cube[1][1][1]]
    f3c1 = [cube[2][0][1], cube[2][1][1]]
    f5r0 = []
    f5r1 = []
    f5r0.append(cube[5][1][0])
    f5r0.append(cube[5][0][0])
    f5r1.append(cube[5][1][1])
    f5r1.append(cube[5][0][1])
    columns = {0:f0c1 , 1:f1c1 , 2:f2c1, 3:f3c1}
    for face in columns:
        cube[face][0][1] = columns[face][0]
        cube[face][1][1] = columns[face][1]
    cube[5][0] = f5r0
    cube[5][1] = f5r1

def top_c():
    global cube
    f1r0 = [cube[5][1][0], cube[5][0][0]]
    f4c1 = cube[1][0]
    f3r1 = [cube[4][0][1], cube[4][1][1]]
    f5c0 = cube[3][1]
    f0r0 = []
    f0r1 = []
    f0r0 = [cube[0][1][0], cube[0][0][0]]
    f0r1 = [cube[0][1][1], cube[0][0][1]]
    cube[5][0][0] = f5c0[0]
    cube[5][1][0] = f5c0[1]
    cube[4][0][1] = f4c1[0]
    cube[4][1][1] = f4c1[1]
    cube[1][0] = f1r0
    cube[3][1] = f3r1
    cube[0][0] = f0r0
    cube[0][1] = f0r1

def top_counterc():
    global cube
    f1r0 = [cube[4][0][1], cube[4][1][1]]
    f4c1 = cube[3][1]
    f3r1 = [cube[5][1][0], cube[5][0][0]]
    f5c0 = cube[1][0]
    f0r0 = []
    f0r1 = []
    f0r0 = [cube[0][0][1], cube[0][1][1]]
    f0r1 = [cube[0][0][0], cube[0][1][0]]
    cube[5][0][0] = f5c0[0]
    cube[5][1][0] = f5c0[1]
    cube[4][0][1] = f4c1[0]
    cube[4][1][1] = f4c1[1]
    cube[1][0] = f1r0
    cube[3][1] = f3r1
    cube[0][0] = f0r0
    cube[0][1] = f0r1

def bottom_c():
    global cube
    f1r1 = [cube[5][0][1], cube[5][1][1]]
    f4c0 = cube[1][1]
    f3r0 = [cube[4][0][0], cube[4][1][0]]
    f5c1 = cube[3][0]
    f2r0 = []
    f2r1 = []
    f2r0 = [cube[2][0][1], cube[2][1][1]]
    f2r1 = [cube[2][0][0], cube[2][1][0]]
    cube[5][0][1] = f5c1[0]
    cube[5][1][1] = f5c1[1]
    cube[4][0][0] = f4c0[0]
    cube[4][1][0] = f4c0[1]
    cube[1][1] = f1r1
    cube[3][0] = f3r0
    cube[2][0] = f2r0
    cube[2][1] = f2r1

def bottom_counterc():
    global cube
    f1r1 = [cube[4][0][0], cube[4][1][0]]
    f4c0 = cube[3][0]
    f3r0 = [cube[5][0][1], cube[5][1][1]]
    f5c1 = cube[1][1]
    f2r0 = []
    f2r1 = []
    f2r0 = [cube[2][0][0], cube[2][1][0]]
    f2r1 = [cube[2][0][1], cube[2][1][1]]
    cube[5][0][1] = f5c1[0]
    cube[5][1][1] = f5c1[1]
    cube[4][0][0] = f4c0[0]
    cube[4][1][0] = f4c0[1]
    cube[1][1] = f1r1
    cube[3][0] = f3r0
    cube[2][0] = f2r0
    cube[2][1] = f2r1

#ask for moves
print_cube()
while True:
    which = input('row, column or spin? ')
    if which == 'row':
        row_num = input('which row (0/1)? ')
        l_r = input('left or right (l/r)? ')
        if row_num == '0':
            if l_r == 'r':
                row0_right()
            elif l_r == 'l':
                row0_left()
            else:
                print('error')
        elif row_num == '1':
            if l_r == 'r':
                row1_right()
            elif l_r == 'l':
                row1_left()
            else:
                print('error')
        else:
            print('error')
    elif which == 'column':
        col_num = input('which column (0/1)? ')
        u_d = input('up or down (u/d)? ')
        if col_num == '0':
            if u_d == 'u':
                col0_up()
            elif u_d == 'd':
                col0_down()
            else:
                print('error')
        elif col_num == '1':
            if u_d == 'u':
                col1_up()
            elif u_d == 'd':
                col1_down()
            else:
                print('error')
        else:
            print('error')
    elif which == 'spin':
        t_b = input('top or bottom (t/b)? ')
        direction = input('which way (c/cc)? ')
        if t_b == 't':
            if direction == 'c':
                top_c()
            elif direction == 'cc':
                top_counterc()
            else:
                print('error')
        if t_b == 'b':
            if direction == 'c':
                bottom_c()
            elif direction == 'cc':
                bottom_counterc()
            else:
                print('error')
        else:
            print('error')
    elif which == 'exit':
        break
    else:
        print('error')
    print_cube()



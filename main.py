str_1 = [' ', ' ', ' ']
str_2 = [' ', ' ', ' ']
str_3 = [' ', ' ', ' ']
print('---------')

print(f'| {str_1[0]} {str_1[1]} {str_1[2]} |')
print(f'| {str_2[0]} {str_2[1]} {str_2[2]} |')
print(f'| {str_3[0]} {str_3[1]} {str_3[2]} |')
print('---------')

def as_int(step):
    try:
        return int(step)
    except ValueError:
        return None

win_count = 0
step_count = 1

while win_count != 1:
    step = input()
    step_list = list(step)
    test_1 = as_int(step_list[0])
    test_2 = as_int(step_list[2])


    if test_1 is None or test_2 is None:
        print('You should enter numbers!')
    else:
        int_cord_1 = int(step_list[0])
        int_cord_2 = int(step_list[2])
        if (int_cord_1 > 3 or int_cord_1 < 1)\
                or (int_cord_2 > 3 or int_cord_2 < 1):
                    print('Coordinates should be from 1 to 3!')
        elif int_cord_1 == 1 and step_count % 2 == 1:
            if str_1[int_cord_2 - 1] == ' ' or str_1[int_cord_2 - 1] == '_':
                str_1[int_cord_2 - 1] = 'X'
                print('---------')
                print(f'| {str_1[0]} {str_1[1]} {str_1[2]} |')
                print(f'| {str_2[0]} {str_2[1]} {str_2[2]} |')
                print(f'| {str_3[0]} {str_3[1]} {str_3[2]} |')
                print('---------')
                step_count += 1
            else:
                print('This cell is occupied! Choose another one!')
        elif int_cord_1 == 2 and step_count % 2 == 1:
            if str_2[int_cord_2 - 1] == ' ' or str_2[int_cord_2 - 1] == '_':
                str_2[int_cord_2 - 1] = 'X'
                print('---------')
                print(f'| {str_1[0]} {str_1[1]} {str_1[2]} |')
                print(f'| {str_2[0]} {str_2[1]} {str_2[2]} |')
                print(f'| {str_3[0]} {str_3[1]} {str_3[2]} |')
                print('---------')
                step_count += 1
            else:
                print('This cell is occupied! Choose another one!')
        elif int_cord_1 == 3 and step_count % 2 == 1:
            if str_3[int_cord_2 - 1] == ' ' or str_3[int_cord_2 - 1] == '_':
                str_3[int_cord_2 - 1] = 'X'
                print('---------')
                print(f'| {str_1[0]} {str_1[1]} {str_1[2]} |')
                print(f'| {str_2[0]} {str_2[1]} {str_2[2]} |')
                print(f'| {str_3[0]} {str_3[1]} {str_3[2]} |')
                print('---------')
                step_count += 1
            else:
                print('This cell is occupied! Choose another one!')

        elif int_cord_1 == 1 and step_count % 2 == 0:
            if str_1[int_cord_2 - 1] == ' ' or str_1[int_cord_2 - 1] == '_':
                str_1[int_cord_2 - 1] = 'O'
                print('---------')
                print(f'| {str_1[0]} {str_1[1]} {str_1[2]} |')
                print(f'| {str_2[0]} {str_2[1]} {str_2[2]} |')
                print(f'| {str_3[0]} {str_3[1]} {str_3[2]} |')
                print('---------')
                step_count += 1
            else:
                print('This cell is occupied! Choose another one!')
        elif int_cord_1 == 2 and step_count % 2 == 0:
            if str_2[int_cord_2 - 1] == ' ' or str_2[int_cord_2 - 1] == '_':
                str_2[int_cord_2 - 1] = 'O'
                print('---------')
                print(f'| {str_1[0]} {str_1[1]} {str_1[2]} |')
                print(f'| {str_2[0]} {str_2[1]} {str_2[2]} |')
                print(f'| {str_3[0]} {str_3[1]} {str_3[2]} |')
                print('---------')
                step_count += 1
            else:
                print('This cell is occupied! Choose another one!')
        elif int_cord_1 == 3 and step_count % 2 == 0:
            if str_3[int_cord_2 - 1] == ' ' or str_3[int_cord_2 - 1] == '_':
                str_3[int_cord_2 - 1] = 'O'
                print('---------')
                print(f'| {str_1[0]} {str_1[1]} {str_1[2]} |')
                print(f'| {str_2[0]} {str_2[1]} {str_2[2]} |')
                print(f'| {str_3[0]} {str_3[1]} {str_3[2]} |')
                print('---------')
                step_count += 1
            else:
                print('This cell is occupied! Choose another one!')

    all_list = []
    for i in range(len(str_1)):
        all_list.append(str_1[i])

    for i in range(len(str_2)):
        all_list.append(str_2[i])

    for i in range(len(str_3)):
        all_list.append(str_3[i])

    count_x = 0
    count_o = 0
    count_space = 0
    count_line = 0

    win_var_1 = [all_list[0], all_list[1], all_list[2]]
    win_var_2 = [all_list[3], all_list[4], all_list[5]]
    win_var_3 = [all_list[6], all_list[7], all_list[8]]
    win_var_4 = [all_list[0], all_list[3], all_list[6]]
    win_var_5 = [all_list[1], all_list[4], all_list[7]]
    win_var_6 = [all_list[2], all_list[5], all_list[8]]
    win_var_7 = [all_list[0], all_list[4], all_list[8]]
    win_var_8 = [all_list[2], all_list[4], all_list[6]]

    win_count_o = 0
    win_count_x = 0

    for i in range(len(all_list)):
        if all_list[i] == 'X':
            count_x += 1
        if all_list[i] == 'O':
            count_o += 1
        if all_list[i] == ' ':
            count_space += 1
        if all_list[i] == '_':
            count_line += 1

    if 'X' not in win_var_1 and '_' not in win_var_1 and ' ' not in win_var_1:
        win_count_o += 1

    if 'X' not in win_var_2 and '_' not in win_var_2 and ' ' not in win_var_2:
        win_count_o += 1

    if 'X' not in win_var_3 and '_' not in win_var_3 and ' ' not in win_var_3:
        win_count_o += 1

    if 'X' not in win_var_4 and '_' not in win_var_4 and ' ' not in win_var_4:
        win_count_o += 1

    if 'X' not in win_var_5 and '_' not in win_var_5 and ' ' not in win_var_5:
        win_count_o += 1

    if 'X' not in win_var_6 and '_' not in win_var_6 and ' ' not in win_var_6:
        win_count_o += 1

    if 'X' not in win_var_7 and '_' not in win_var_7 and ' ' not in win_var_7:
        win_count_o += 1

    if 'X' not in win_var_8 and '_' not in win_var_8 and ' ' not in win_var_8:
        win_count_o += 1

    if 'O' not in win_var_1 and '_' not in win_var_1 and ' ' not in win_var_1:
        win_count_x += 1

    if 'O' not in win_var_2 and '_' not in win_var_2 and ' ' not in win_var_2:
        win_count_x += 1

    if 'O' not in win_var_3 and '_' not in win_var_3 and ' ' not in win_var_3:
        win_count_x += 1

    if 'O' not in win_var_4 and '_' not in win_var_4 and ' ' not in win_var_4:
        win_count_x += 1

    if 'O' not in win_var_5 and '_' not in win_var_5 and ' ' not in win_var_5:
        win_count_x += 1

    if 'O' not in win_var_6 and '_' not in win_var_6 and ' ' not in win_var_6:
        win_count_x += 1

    if 'O' not in win_var_7 and '_' not in win_var_7 and ' ' not in win_var_7:
        win_count_x += 1

    if 'O' not in win_var_8 and '_' not in win_var_8 and ' ' not in win_var_8:
        win_count_x += 1

    if win_count_x > win_count_o:
        print('X wins')
        win_count = 1

    elif win_count_o > win_count_x:
        print('O wins')
        win_count = 1

    elif (win_count_o == win_count_x) and (count_line == 0 and count_space == 0):
        print('Draw')
        win_count = 1

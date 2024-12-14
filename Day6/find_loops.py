# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_loops.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bebuber <bebuber@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/11 15:14:22 by bebuber           #+#    #+#              #
#    Updated: 2024/12/14 17:02:49 by bebuber          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import copy

def read_file(file_path):
    with open(file_path, 'r') as file:
        return[list(line.strip()) for line in file]

def find_starting_point(map_data):
    directions = {'^': "up", 'v': "down", '<': "left", '>': "right"}
    for i, row in enumerate(map_data):
        for j, cell in enumerate(row):
            if cell in directions:
                return (i, j), directions[cell]
    return None, None

def turn_right(direction):
    if direction == "up":
        return "right"
    elif direction == "right":
        return "down"
    elif direction == "down":
        return "left"
    elif direction == "left":
        return "up"

def step_up(x, y, direction):
    if direction == "up":
        return x - 1, y
    elif direction == "right":
        return x, y + 1
    elif direction == "down":
        return x + 1, y
    elif direction == "left":
        return x, y - 1

def path_length(map_data):
    path_length = 0
    for x, row in enumerate(map_data):
        for y, cell in enumerate(row):
            if cell in {'-','|', '+', '^'}:
                path_length += 1            
    return path_length

def mark_the_route(map_data, x, y, direction):
    if direction in {'right', 'left'}:
        if map_data[x][y] == '|':
            map_data[x][y] = '+'
        elif map_data[x][y] in {'-', '+'}:
            return -1
        else:
            map_data[x][y] = '-'
    elif direction in {'up', 'down'}:
        if map_data[x][y] == '-':
            map_data[x][y] = '+'
        elif map_data[x][y] in {'|', '+'}:
            return -1
        else:
            map_data[x][y] = '|'
    return 1


def move_guard(map_data, start, direction):
    x, y = start
    save_path = set()

    while 0 <= x < len(map_data) and 0 <= y < len(map_data[0]):
        next_x, next_y = step_up(x, y, direction)
        if 0 <= next_x < len(map_data) and 0 <= next_y < len(map_data[0]):
            mark_the_route(map_data, x, y, direction)
            if (x, y, direction) in save_path:
                return -1
            save_path.add((x, y, direction))
            if map_data[next_x][next_y] in {'.', '^', '+', '-', '|'}:
                x, y = next_x, next_y
                mark_the_route(map_data, x, y, direction)
            else:
                direction = turn_right(direction)
        else:
            break
    return 1

def write_file(file_path, map_data):
    with open(file_path, 'w') as file:
        for row in map_data:
            file.write(''.join(row) + '\n')



def find_loops_with_obstacle(map_data, start, direction):
    loop_count = 0
    x, y = start
    i = 0
    tried_locations = set()
    tried_locations.add((x, y))
    
    while 0 <= x < len(map_data) and 0 <= y < len(map_data[0]):
        map_copy = copy.deepcopy(map_data)
        if map_copy[x][y] == '.' and (x, y) not in tried_locations:
            i += 1
            tried_locations.add((x, y))
            map_copy[x][y] = 'O'
            if move_guard(map_copy, start, 'up') == -1:
                loop_count += 1
    
        next_x, next_y = step_up(x, y, direction)
        if 0 <= next_x < len(map_data) and 0 <= next_y < len(map_data[0]):
            while (map_data[next_x][next_y] == '#'):
                direction = turn_right(direction)
                next_x, next_y = step_up(x, y, direction)
                if not 0 <= next_x < len(map_data) and 0 <= next_y < len(map_data[0]):
                    return loop_count
            if map_data[next_x][next_y] in {'.', '^'}:
                x, y = next_x, next_y                
        else:
            break
    print ("times loop runed:",(i))
    return loop_count



def main():
    file_path = 'example.txt'
    map_data = read_file(file_path)
    start, direction = find_starting_point(map_data)

    loup_count = find_loops_with_obstacle(map_data, start, direction)
    print("loop count: ",(loup_count))
    
    # write_file("find_loops.txt", map_copy)
    # path_length = path_length(map_data)
    # print("Path length:", path_length)
    
    # for line in map_data:
    #     print(''.join(line))


if __name__ == "__main__":
    main()
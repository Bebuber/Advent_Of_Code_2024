# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_the_path.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bebuber <bebuber@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/11 15:14:22 by bebuber           #+#    #+#              #
#    Updated: 2024/12/14 16:18:49 by bebuber          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
            if cell == 'X':
                path_length += 1            
    return path_length

def move_guard(map_data, start, direction):
    x, y = start

    map_data[x][y] = "X"
    while 0 <= x < len(map_data) and 0 <= y < len(map_data[0]):
        next_x, next_y = step_up(x, y, direction)
        if 0 <= next_x < len(map_data) and 0 <= next_y < len(map_data[0]):
            if map_data[next_x][next_y] == '.' or map_data[next_x][next_y] == "X":
                x, y = next_x, next_y
                map_data[x][y] = 'X'
            else:
                direction = turn_right (direction)
        else:
            break
    return path_length(map_data)

def write_file(file_path, map_data):
    with open(file_path, 'w') as file:
        for row in map_data:
            file.write(''.join(row) + '\n')
            
def main():
    file_path = 'map.txt'
    map_data = read_file(file_path)
    start, direction = find_starting_point(map_data)

    if (start is None or direction is None):
        print("Starting point not found.")
        return

    path_length = move_guard(map_data, start, direction)
    print("Path length:", path_length)
    
    write_file("path_of_guard.txt", map_data)

if __name__ == "__main__":
    main()
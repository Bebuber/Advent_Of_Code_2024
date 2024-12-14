# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    x_mas_finder.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bebuber <bebuber@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/09 13:31:23 by bebuber           #+#    #+#              #
#    Updated: 2024/12/11 13:18:32 by bebuber          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def search_x_mas_pattern(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    # Iterate over each possible center position of the "X-MAS" pattern
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if (grid[row][col] == 'A'):
                if (grid[row - 1][col - 1] == 'M' and grid[row - 1][col + 1] == 'S' and
                    grid[row + 1][col - 1] == 'M' and grid[row + 1][col + 1] == 'S'):
                    count += 1                
                if (grid[row - 1][col - 1] == 'S' and grid[row - 1][col + 1] == 'M' and
                    grid[row + 1][col - 1] == 'S' and grid[row + 1][col + 1] == 'M'):
                    count += 1
                if (grid[row - 1][col - 1] == 'M' and grid[row - 1][col + 1] == 'M' and
                    grid[row + 1][col - 1] == 'S' and grid[row + 1][col + 1] == 'S'):
                    count += 1
                if (grid[row - 1][col - 1] == 'S' and grid[row - 1][col + 1] == 'S' and
                    grid[row + 1][col - 1] == 'M' and grid[row + 1][col + 1] == 'M'):
                    count += 1    
    return count

def main():
    file_path = 'XMAS.csv'  # Replace with your grid file path
    grid = read_grid(file_path)
    result = search_x_mas_pattern(grid)
    print(f"Total instances of 'X-MAS' pattern: {result}")

if __name__ == "__main__":
    main()
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_all_xmases.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bebuber <bebuber@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/09 13:06:56 by bebuber           #+#    #+#              #
#    Updated: 2024/12/09 13:18:52 by bebuber          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def search_horizontal(grid, word):
    count = 0
    word_len = len(word)
    for row in grid:
        for i in range(len(row) - word_len + 1):
            if row[i:i + word_len] == word:
                count += 1
            if row[i:i + word_len] == word[::-1]:
                count += 1
    return count

def search_vertical(grid, word):
    count = 0
    word_len = len(word)
    for col in range(len(grid[0])):
        for row in range(len(grid) - word_len + 1):
            vertical_word = ''.join(grid[row + i][col] for i in range(word_len))
            if vertical_word == word:
                count += 1
            if vertical_word == word[::-1]:
                count += 1
    return count

def search_diagonal(grid, word):
    count = 0
    word_len = len(word)
    rows = len(grid)
    cols = len(grid[0])
    
    # Top-left to bottom-right and bottom-right to top-left
    for row in range(rows - word_len + 1):
        for col in range(cols - word_len + 1):
            diagonal_word = ''.join(grid[row + i][col + i] for i in range(word_len))
            if diagonal_word == word:
                count += 1
            if diagonal_word == word[::-1]:
                count += 1
    
    # Top-right to bottom-left and bottom-left to top-right
    for row in range(rows - word_len + 1):
        for col in range(word_len - 1, cols):
            diagonal_word = ''.join(grid[row + i][col - i] for i in range(word_len))
            if diagonal_word == word:
                count += 1
            if diagonal_word == word[::-1]:
                count += 1
    
    return count

def count_xmas(grid):
    word = "XMAS"
    total_count = 0
    total_count += search_horizontal(grid, word)
    total_count += search_vertical(grid, word)
    total_count += search_diagonal(grid, word)
    return total_count

def main():
    file_path = 'test.csv'  # Replace with your grid file path
    grid = read_grid(file_path)
    result = count_xmas(grid)
    print(f"Total instances of 'XMAS': {result}")

if __name__ == "__main__":
    main()
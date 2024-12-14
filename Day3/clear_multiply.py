# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    clear_multiply.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bebuber <bebuber@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/07 18:28:23 by bebuber           #+#    #+#              #
#    Updated: 2024/12/07 21:26:41 by bebuber          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def extract_and_sum_multiplications(data):
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    matches = pattern.findall(data)
    
    total_sum = 0
    for match in matches:
        x, y = int(match[0]), int(match[1])
        total_sum += x * y
    
    return total_sum

file_path = 'CORRUPTED_MEMORY.CSV'
data = read_csv_file(file_path)
result = extract_and_sum_multiplications(data)

print(f"Total sum of all valid multiplications: {result}") 
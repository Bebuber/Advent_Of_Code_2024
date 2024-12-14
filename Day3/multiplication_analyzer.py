# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multiplication_analyzer.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bebuber <bebuber@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/07 19:36:10 by bebuber           #+#    #+#              #
#    Updated: 2024/12/09 12:54:26 by bebuber          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def extract_and_sum_multiplications(data):
    # Regular expressions to match valid instructions
    mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r'don\'t\(\)')
    
    total_sum = 0
    segments = re.split(r'(do\(\)|don\'t\(\))', data)
    
    process_segment = True
    
    for segment in segments:
        segment = segment.strip()
        if do_pattern.match(segment):
            process_segment = True
            # print(f"do() found, enabling mul: {segment}")
        elif dont_pattern.match(segment):
            process_segment = False
            # print(f"don't() found, disabling mul: {segment}")
        elif process_segment:
            matches = mul_pattern.findall(segment)
            for match in matches:
                x, y = int(match[0]), int(match[1])
                total_sum += x * y
                # print(f"mul({x},{y}) found, adding {x * y} to total_sum: {total_sum}")
    
    return total_sum

def main():
    file_path = 'CORRUPTED_MEMORY.CSV'
    data = read_csv_file(file_path)
    result = extract_and_sum_multiplications(data)
    print(f"Total sum of all valid multiplications: {result}")

if __name__ == "__main__":
    main()
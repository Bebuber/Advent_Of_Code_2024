# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    order_all_pages.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bebuber <bebuber@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/11 14:33:58 by bebuber           #+#    #+#              #
#    Updated: 2024/12/11 15:02:22 by bebuber          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv
from functools import cmp_to_key

def read_csv_file(file_path):
    rules = []
    updates = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='|')
        reading_updates = False
        for row in reader:
            if not row:  # Skip empty rows
                continue
            if len(row) == 1 and ',' in row[0]:
                reading_updates = True
            if reading_updates:
                updates.append([int(num) for num in row[0].split(',')])
            else:
                rules.append([int(num) for num in row])
    return rules, updates

def parse_input(file_path):
    rules, updates = read_csv_file(file_path)
    return rules, updates

def is_update_correct(update, rules):
    index_map = {page: idx for idx, page in enumerate(update)}
    for before, after in rules:
        if before in index_map and after in index_map:
            if index_map[before] > index_map[after]:
                return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def compare_pages(page1, page2, rules):
    for before, after in rules:
        if before == page1 and after == page2:
            return -1
        if before == page2 and after == page1:
            return 1
    return 0

def correct_order(update, rules):
    return sorted(update, key=cmp_to_key(lambda x, y: compare_pages(x, y, rules)))

def main():
    file_path = 'PAGES.csv'
    rules, updates = parse_input(file_path)
    middle_pages_sum = 0
    corrected_middle_pages_sum = 0

    for update in updates:
        if is_update_correct(update, rules):
            middle_pages_sum += find_middle_page(update)
        else:
            corrected_update = correct_order(update, rules)
            corrected_middle_pages_sum += find_middle_page(corrected_update)

    print("Sum of middle pages:", middle_pages_sum)
    print("Sum of corrected middle pages:", corrected_middle_pages_sum)
    print("Total sum:", middle_pages_sum + corrected_middle_pages_sum)
	
if __name__ == "__main__":
    main()
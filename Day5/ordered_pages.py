# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ordered_pages.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bebuber <bebuber@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/11 13:27:10 by bebuber           #+#    #+#              #
#    Updated: 2024/12/14 17:38:23 by bebuber          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv

def read_csv_file(file_path):
    rules = []
    updates = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='|')
        reading_updates = False
        for row in reader:
            if not row:
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

def main():
    file_path = 'PAGES.csv'
    rules, updates = parse_input(file_path)
    middle_pages_sum = 0

    for update in updates:
        if is_update_correct(update, rules):
            middle_pages_sum += find_middle_page(update)

    print(middle_pages_sum)

if __name__ == "__main__":
    main()
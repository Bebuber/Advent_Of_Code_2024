# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    analyzing_reports.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bebuber <bebuber@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/07 17:49:30 by bebuber           #+#    #+#              #
#    Updated: 2024/12/07 18:06:08 by bebuber          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            data.append([int(num) for num in row])
    return data

def is_safe_report(report):
    increasing = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def count_safe_reports(data):
    safe_count = 0
    for report in data:
        if is_safe_report(report):
            safe_count += 1
    return safe_count

file_path = 'REPORTS.CSV'
data = read_csv_file(file_path)
safe_reports_count = count_safe_reports(data)

print("Number of safe reports: {}".format(safe_reports_count))
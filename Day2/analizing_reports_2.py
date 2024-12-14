# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    analizing_reports_2.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bebuber <bebuber@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/07 18:13:22 by bebuber           #+#    #+#              #
#    Updated: 2024/12/07 18:22:22 by bebuber          ###   ########.fr        #
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
    def check_increasing_or_decreasing(sub_report):
        increasing = all(sub_report[i] < sub_report[i + 1] and 1 <= sub_report[i + 1] - sub_report[i] <= 3 for i in range(len(sub_report) - 1))
        decreasing = all(sub_report[i] > sub_report[i + 1] and 1 <= sub_report[i] - sub_report[i + 1] <= 3 for i in range(len(sub_report) - 1))
        return increasing or decreasing

    if check_increasing_or_decreasing(report):
        return True

    for i in range(len(report)):
        sub_report = report[:i] + report[i+1:]
        if check_increasing_or_decreasing(sub_report):
            return True

    return False

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

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    total_calibration_result.py                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bebuber <bebuber@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/14 17:12:20 by bebuber           #+#    #+#              #
#    Updated: 2024/12/14 17:48:08 by bebuber          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from itertools import product
import re
	
def parse_equations(file_path):
	equations = []
	with open(file_path, 'r') as file:
		for line in file:
			parts = re.split(r':\s*|\s', line.strip())
			test_value = int(parts[0])
			numbers = list(map(int, parts[1:]))
			equations.append((test_value, numbers))
	return equations

def evaluate_expression(numbers, operators):
	result = numbers[0]
	for i in range(len(operators)):
		if operators[i] == '+':
			result += numbers[i + 1]
		elif operators[i] == '*':
			result *= numbers[i + 1]
	return result

def can_be_true(test_value, numbers):
	n = len(numbers) - 1
	for ops in product('+*', repeat=n):
		if evaluate_expression(numbers, ops) == test_value:
			return True
	return False

def total_calibration_result(equations):
	total = 0
	for equation in equations:
		test_value, numbers = equation
		if can_be_true(test_value, numbers):
			total += test_value
	return total

def main():
	file_path = "equations.csv"
	equations = parse_equations(file_path)
	print(total_calibration_result(equations))
		
if __name__ == "__main__":
    main()
	
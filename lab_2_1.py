#sqrt_decomposition

import sys
import argparse
import math

def sum_sqrt(array, start, end):
	sum = 0
	length = len(array)
	n_length = int(math.ceil(math.sqrt(length)))
	n_array = [0 for _ in range(n_length)]

	for _ in range(length):				#sums of blocks
		n_array[_ // n_length] += array[_] 

	while start <= end:
		if (start % n_length == 0) and (start + n_length-1 <= end):
			sum += n_array[start // n_length]
			start += n_length;
		else:
			sum += array[start]
			start += 1
	return sum

def sum_chek(array, start, end):
	sum = 0
	for x in range(start, end+1):
		sum += array[x]
	return sum

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--args', nargs='+', type=int, help='input array')
parser.add_argument('-s', type=int, help='start point')
parser.add_argument('-e', type=int, help='end point')
parser.add_argument('-c','--chek', type=bool, help='if you need to chek')
parser.add_argument('-f', '--file', type=bool, help='if you need to input from file')

inputs = parser.parse_args()
array = inputs.args
start = inputs.s
end = inputs.e

flag1 = inputs.chek
flag2 = inputs.file

if flag2:
	file = open('additional/for_first.txt','r')
	array = file.read().split(' ')
	array = [int(_) for _ in array]
	file.close()

print(sum_sqrt(array, start, end))
if flag1:
	print(sum_chek(array, start, end))

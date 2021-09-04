import argparse
import math

def is_power_of2(n):
	if n == 0:
		return False
	return math.log(n, 2).is_integer()

def is_power_of2_chek(n):
	if n == 0:
		return False
	if n.is_integer():
		n = int(n)
		return n & (n-1) == 0
	return False


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', '--number', type=int, help='input non negative number')
	parser.add_argument('-c','--chek', type=bool, help='True/False if you need to chek')
	inputs = parser.parse_args()


	n = inputs.number

	if n is None or n < 0:
		n = -1
		while n < 0:
			print("input non negative number")
			n = input()
			if n.isdigit():
				n = int(n)
				break
			n = -1

	print(is_power_of2(n))
	if inputs.chek:
		print(is_power_of2_chek(n))

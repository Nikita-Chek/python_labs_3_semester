import argparse
import math

fi = (1 + math.sqrt(5)) / 2
psi = (1 - math.sqrt(5)) / 2

def leonardo_number(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	return leonardo_number(n-1) + leonardo_number(n-2) + 1  

def fibonacci(n):
	return int((fi**n - psi**n) / math.sqrt(5))

def leonardo_chek(n):
	return 2 * fibonacci(n+1) - 1


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

	print('leonardo_number:', leonardo_number(n))

	if inputs.chek:
		print( leonardo_chek(n) )

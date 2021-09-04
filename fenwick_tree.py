array = input("input array: ").split()
start = int(input("start: "))-1
end = int(input("end: "))

for _ in range(len(array)):     #from input string array to int array
	array[_] = int(array[_])


def fenwick(x):
	return x & (x+1)

def sum(array, x):
	fen_ = 0
	for _ in range(fenwick(x), x+1):
		fen_ += array[_]
	return fen_ 

def fenwick_sum(array, start, end):
	fen = []
	for _ in range(len(array)):
		fen.append(sum(array, _))
	sum_ = 0

	while (end >= 0):
		sum_ += fen[end];
		end = fenwick(end) - 1;
	
	while (start >= 0):
		sum_ -= fen[start];
		start = fenwick(start) - 1;
	
	return sum_;

print(fenwick_sum(array, start, end))

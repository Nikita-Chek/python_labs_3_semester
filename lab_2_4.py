import argparse
import json
import os

def flatten(List, fl = []):
	for _ in List:
		if type(List[_]) is list:
			flatten(List[_], fl)
		else:
			fl.append(List[_])
	return fl

def gen_flatten(List):
	for _ in List:
		if type(_) is list:
			yield from gen_flatten(_)
		else:
			yield _


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', type=str)
	file = parser.parse_args().file
	with open('additional/array_json.json', 'r') as f:
		data = json.load(f)

	List = data[""]
	#List = [[2,3], [3, 3, 'er'], [[4], [3,[[6,[3],5,2]]]], [[[6]]]]

	l = []
	for _ in gen_flatten(List):
		l.append(_)
	print(l)

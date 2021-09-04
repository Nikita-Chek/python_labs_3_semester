import json
import jsonpickle
import re

Set = set()

def add(*objects):
	for _ in objects:
		Set.add(_)

def list():
	print(Set)

def remove(object):
	Set.discard(object)

def find(*object):
	for _ in object:
		if _ in Set:
			print(_, "  type is: ", type(_))
		else:
			print("ValueNotFound")

def save():
	Set_save = jsonpickle.encode(Set)
	with open("additional/for_ten.json", "w") as write_file:
		json.dump(Set_save, write_file)

def load():
	global Set
	with open("additional/for_ten.json", "r") as read_file:
		Set_load = json.load(read_file)
		Set = jsonpickle.decode(Set_load)

def grep(string):
	string = string + r'\S*'
	for _ in Set:
		_ = str(_)
		result = re.findall(string, _)
		if result != []:
			print(result)
			
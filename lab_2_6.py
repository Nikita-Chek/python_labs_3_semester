import re

file = open('additional/for_five.json', 'r')
js = file.read()
js = re.sub(r'[\s]', r'', js)
file.close()

json_regex = re.compile(r'[:].+', re.DOTALL)
float_regex = re.compile(r'^[+-]?\d*[.,]\d*$')
int_regex = re.compile(r'^[+-]?\d+$')
str_regex = re.compile(r'\".*\"')
list_regex = re.compile(r'^\[.+\]$')

match = json_regex.search(js)
js = match[0]
js = js[1:-1]
print(js, '\n')


def from_json(Object):
	if Object == 'true':
		return True
	if Object == 'false':
		return False
	if int_regex.match(Object) is not None:
		return int(Object)
	if float_regex.match(Object) is not None:
		return float(Object)
	if str_regex.match(Object) is not None:
		return Object[1:-1]
	if re.search(r'\[.*\]', Object) is not None:
		return json_to_list(Object)
	return ValueError

def json_to_list(list_, l=[]):
	match = re.search(r'\[', list_)
	if match is None:
		#print(list_)
		return list_

	# list_ = list_[1:-1]
	# list1 = list_
	print(list_)
	if list_[0] == '[':
		list_ = list_[1:-1]
		list1 = list_
		print(list1)
	match = re.search(r'\[', list_)
	if match is not None:
		c, d = 0,0
		t = []
		for _ in range(len(list_)):
			if list_[_] == '[':
				c += 1
				if c == 1:
					i = _

			if list_[_] == ']':
				d += 1
				j = _

			if c and c == d:
				t.append(i)
				t.append(j)
				c,d = 0,0
		for i in range(0,len(t)-1, 2):
			l.append( list_[ t[i]:t[i+1]+1])
			list1  = list1 .replace(list_[ t[i]-1:t[i+1]+1],'', 1)
		list1 = list1 .split(',')
		list1 += l
		l = []
	else:
		list1 = list1.split(',')
	for i in list1:
		#print(i)
		json_to_list(i)

json_to_list("3,[2]")

#print(from_json(js), type(from_json(js)))
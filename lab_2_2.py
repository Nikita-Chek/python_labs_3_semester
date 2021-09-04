import random 
import string
import os
import progressbar
import time
 
bar = progressbar.ProgressBar().start()
 
arguments = input("input: ").split()
alphabet = list(string.ascii_letters)

arguments[0] = int(arguments[0])
for i in [1,2]:
	arguments[i] = [int(_) for _ in list(arguments[i].split(','))]
 

#file_size = os.path.getsize('additional/text.txt')



def generate_file(Mb, K=[10, 100] , L=[3,10]):
	
	while (os.path.getsize('additional/text.txt')/1048576) < Mb:
		k = random.randint(*K)
		i = 0
		t = 0
		while i < k:
			file.write(word(L)+' ')
			i += 1
			bar.update(t)
			t += 0.001
		file.write('\n') 
	return

def word(L):
	word = random.choices(alphabet, 
				  k=random.randint(*L))
	return ''.join(word)

file = open('additional/text.txt', 'w' , encoding='utf-8')
generate_file(*arguments)
bar.finish()
file.close()
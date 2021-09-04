import os
import argparse
import re
from collections import Counter
import statistics
from nltk import ngrams

def words_in_sentence(text):
	sentences = re.split(r'\.', text)
	words_in_sentence = []
	for _ in sentences:
		words_in_sentence.append(_.count(' ') + 1)
	return words_in_sentence

#1
def words_statistic(text):
	words = re.findall(r'\w+', text)
	words = [i.lower() for i in words]
	return Counter(words)

#2
def average(text):
	return statistics.mean(words_in_sentence(text))

#3
def	average_median(text):
	return statistics.median(words_in_sentence(text))

#4
def top_k_ngrams(text, k, n):
	words = re.findall(r'\w+', text)
	words = [i.lower() for i in words]
	all_ngrams = []
	for __ in words:
		n_grams = ngrams(__, n)
		for _ in n_grams:
			all_ngrams.append(''.join(_))
	return Counter(all_ngrams).most_common(k)


def interface(_, text, k, n):
	switcher={'1': words_statistic(text),
	'2': average(text),
	'3': average_median(text),
	'4': top_k_ngrams(text, k, n),
	'exit': 'exit'}
	return switcher.get(_)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-k', '--k', type=int, help='top k', dest='k', default=10)
	parser.add_argument('-n', '--n', type=int, help='n_grams',dest="n", default=4)
	args = parser.parse_args()

	file = open('additional/for_nine.txt','r')
	text = file.read()
	file.close()



#interface
	while True:
		face = input("Choese problem: 1,2,3,4 or type 'exit' to quit: ")
		if interface(face, text, args.k, args.n) == 'exit':
			break
		print(interface(face, text, args.k, args.n))

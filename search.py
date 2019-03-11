#!/home/lion/anaconda3/bin/python3.6

import sys
from base import data

def main():
	if len(sys.argv) <= 1:
		print("Usage: <search.py string | strings to find>")
		exit(0)
	cnt = 0
	maximum = 0
	results = []
	for token in sys.argv:
		for el in data:
			if token in el:
				results.append(el)
	print(results)
	

if __name__ == "__main__":
	main()

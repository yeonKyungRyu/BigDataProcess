#! /usr/bin/python3
import sys

dic={}
input_file=sys.argv[1]
output_file=sys.argv[2]

with open(input_file, "rt") as f:
	for line in f:
		line = line.rstrip()
		str_arr=line.split("::", )
		#print(str_arr)
		genre_arr=str_arr[2].split("|")
		#print(genre_arr)
		for s in genre_arr:
			if s not in dic:
				dic[s] = 1
			else:
				dic[s] += 1

itemlist = dic.items()
with open(output_file, "wt") as f:
	for i in itemlist:
		f.write("%s %s\n" % (i[0], i[1]))

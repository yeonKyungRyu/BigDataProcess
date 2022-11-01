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
		if str_arr[2] not in dic:
			dic[str_arr[2]] = 1
		else:
			dic[str_arr[2]] += 1

itemlist = dic.items()
with open(output_file, "wt") as f:
	for i in itemlist:
		f.write("%s %s\n" % (i[0], i[1]))

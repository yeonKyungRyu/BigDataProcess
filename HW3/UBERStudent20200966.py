#! /usr/bin/python3
import sys
import datetime

days=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
arr=[]
input_file=sys.argv[1]
output_file=sys.argv[2]

with open(input_file, "rt") as f:
	for line in f:
		line = line.rstrip()
		str_arr=line.split(",")
		#print(str_arr)

		number=str_arr[0]
		vehicles=str_arr[2]
		trips=str_arr[3]

		date=str_arr[1].split("/")
		week=days[datetime.date(int(date[2]), int(date[0]), int(date[1])).weekday()]
		new_str= "%s,%s %s,%s" % (number, week, vehicles, trips)
		arr.append(new_str)

#print(arr)
with open(output_file, "wt") as f:
	for str in arr:
		f.write("%s\n" % (str))

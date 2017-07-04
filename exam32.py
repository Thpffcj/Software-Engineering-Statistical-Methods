#encoding=utf-8

import csv
import urllib2
import numpy as np

class Solution():
	def solve(self):
		response_2010 = urllib2.urlopen("http://py.mooctest.net:8081/dataset/temperature/temperature_2010.csv")
		response_2014 = urllib2.urlopen("http://py.mooctest.net:8081/dataset/temperature/temperature_2014.csv")

		csv_reader_2010 = csv.reader(response_2010)
		csv_reader_2014 = csv.reader(response_2014)
		list2010 = [row[8] for row in csv_reader_2010]
		list2014 = [row[8] for row in csv_reader_2014]
		list2010 = list2010[6:-3]
		list2014 = list2014[5:-3]

#		print list2010
		lst = np.array(list2010)
		print float(list2010[0]) + float(list2010[1])
		print lst[0] + lst[1]

if __name__ == '__main__':
	s = Solution()
	s.solve()

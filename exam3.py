#encoding=utf-8
'''
当前世界全球变暖现象严重，为了探索中国是否也存在这个现象，现调查了中国主要城市的全年气温情况，包括2010年全年气温状况与2014年全年气温状况，以8月份气温为例，
假设主要城市温度符合正态分布，试比较是否存在温度上升现象？（需给出证明过程，仅回答YES或NO不得分）
'''
from scipy.stats import t
import numpy as np
import csv
import urllib
import pandas as pd

class Solution():
	def solve(self):
		data1 = pd.read_csv('http://py.mooctest.net:8081/dataset/temperature/temperature_2010.csv', usecols=[8])
		data2 = pd.read_csv('http://py.mooctest.net:8081/dataset/temperature/temperature_2014.csv', usecols=[8])
#		year10 = [25.7, 25.6, 25.6, 22.4, 21.7, 23.3, 23, 22.2, 27.9, 27.2, 28.4, 27.5, 29.3, 29.4, 25.1, 26, 29.1,
#				  29.4, 29.9, 28.8, 28.1, 28.4, 25, 23.6, 20.6, 16.4, 24.7, 18.3, 15.4, 21.3, 22.9]
#		year14 = [27.3, 27.7, 27.9, 23.6, 20.6, 24.3, 22.6, 22.5, 31, 30.8, 31.3, 31.1, 29.6, 31.6, 28.6, 30.1, 30.6,
#				  32, 27.5, 27.7, 27.9, 30.5, 26.5, 23.1, 19.9, 15.9, 28.3, 21, 18.2, 24.4, 22.8]
#		temp_old = urllib.urlopen('http://py.mooctest.net:8081/dataset/temperature/temperature_2010.csv')
#		temp_old = csv.reader(open('http://py.mooctest.net:8081/dataset/temperature/temperature_2010.csv'))
#		temp_new = urllib.urlopen('http://py.mooctest.net:8081/dataset/temperature/temperature_2014.csv')
#		temp_old_data = temp_old.read()
#		temp_new_data = temp_new.read()

		temp_old = data1.values
		temp_new = data2.values
		year10 = np.array(temp_old)[5:36]
		year14 = np.array(temp_new)[4:35]
		print year10[30]
		print year14[30]
#		print float(year14[1][0])
		data = []
		for i in range(31):
			result = float(year10[i][0]) - float(year14[i][0])
			if(result >=0 ):
				data.append(result)
			else:
				data.append(-result)

		data = np.array(data)
		m = data.mean()
		print data

		s = 0.0
		for i in range(31):
			s = s + (data[i]-m)**2
		s = s/31.0
		print s
		result = m*np.sqrt(31)/s
#		print result
		de = t.ppf(0.95, 20)
		if result >= de:
			print 'YES'
			return 'YES'
		else:
			print 'NO'
			return 'NO'

if __name__ == '__main__':
	s = Solution()
	s.solve()

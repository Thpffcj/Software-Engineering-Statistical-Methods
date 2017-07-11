#encoding=utf-8
'''
人口普查是一项重要的国情调查，对于国家管理、制定各项方针政策具有重要的意义，中国最早的一次人口普查在西汉汉平帝元始二年进行，而自中华人民共和国建国以来分别在
1953、1964、1982、1990、2000和2010年进行了共六次人口普查，其中第六次人口普查分别涉及到了人口增长、家庭户人口、性别构成、年龄构成、民族构成、受教育程度、城乡人口、
人口流动性等八方面。现有《各地区分性别、健康状况的60岁及以上老年人口》调查数据、《各地区户数、人口数和性别比》调查数据，定义老龄率=60岁及以上人口数*100/总人口数，
以北京市为例，其老龄率为250084*100/1849475=13.52，请编写python代码回答如下问题：

以各省市数据为代表，求取中国省级老龄率均值的置信区间、方差的置信区间，置信水平均为90%，假设老龄率符合正态分布
'''
import numpy as np
import csv
from scipy.stats import t
from scipy.stats import norm
from scipy.stats import chi2
import pandas as pd

class Solution():
	def solve(self):
		popu_old = [250084, 162233, 928642, 414649, 275828, 672227, 349177, 468616, 345592, 1247962, 759091, 853195,
					420377, 504043, 1400109, 1196924, 779566, 939818, 957360, 616828, 93525, 488115, 1412294, 446686,
					514563, 20828, 487378, 338325, 51945, 61207, 201515]
		popu_total = [1849475, 1127589, 7037620, 3477805, 2310941, 4252076, 2551123, 3465051, 2253525, 7577122, 5400348,
					  5312628, 3477491, 4251692, 9272503, 9224288, 5226904, 6096586, 9676589, 4362551, 826560, 2609882,
					  8161604, 3332265, 4467537, 265904, 3614887, 2623094, 535412, 611957, 2086576]
		data1 = pd.read_csv('http://py.mooctest.net:8081/dataset/population/population_old.csv',usecols=[1])
		data2 = pd.read_csv('http://py.mooctest.net:8081/dataset/population/population_total.csv', usecols=[4])
#		print data
		list1 = []
		list2 = []
		d1 = data1.values
		d2 = data2.values
		for i in range(2,33):
			s1 = d1[i][0]
			list1.append(s1)
		for i in range(4, 35):
			s2 = d2[i][0]
			list2.append(s2)
		np_lst = np.array(list2)
		print np_lst
#		print list[30]
#		print data
#		population_old = csv.reader(open('population_old.csv'))
#		population_total = csv.DictReader(open('population_total.csv'))
#		population_old_data = []
#		population_total_data = []
#		m1 = 0
#		for row1 in population_old:
#			population_old_data[m1] = row1[3]
#			m1 = m1 + 1
#		m2 = 0
#		for row2 in population_total:
#			population_total_data[m2] = row2
#			m2 = m2 + 1
		de3 = norm.ppf(0.95)
		print de3
		de = t.ppf(0.95, 30)
		print de
		result = 0.0
		data = []
		for i in range(31):
			data.append((float(list1[i])*100.0/float(list2[i])))
		print data[0]
		for i in range(31):
			result = result + data[i]
		result = result/31.0
		print result
		s = 0.0
		for i in range(31):
			s = s + (data[i]-result)**2
		s = s/31.0
		s = np.sqrt(s)
		print s
		ave1 = result - s*de3/np.sqrt(31)
		ave2 = result + s*de3/np.sqrt(31)
		de1 = chi2.ppf(0.05, 30)
		de2 = chi2.ppf(0.95, 30)
		s1 = 30*s*s/de2
		s2 = 30*s*s/de1
		print [[ave1, ave2], [s1, s2]]
		return [[ave1, ave2], [s1, s2]]

if __name__ == '__main__':
	s = Solution()
	s.solve()

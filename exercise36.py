#-*- coding:utf-8 -*-
'''
The table below summaries a data set that examines the response of a random sample of college graduates and non-graduate on the topic of oil drilling.
Complete a chi-square test for test data to check whether there is a statistically significant difference in responses from college graduates and non-graduates.
# College Grad? 	Yes 	No 	    Total
# Support 	        154 	132 	286
# Oppose 	        180 	126 	306
# Do not know 	    104 	131 	235
# Total 	        438 	389 	827
下表汇总了一个数据集，用于检查大学毕业生和非毕业生随机抽样的石油钻探专题的回答。
完成测试数据的卡方测试，以检查大学毕业生和非毕业生的回应是否有统计学差异。
'''
from scipy.stats import chi2
import numpy as np
import csv

class Solution():
	def solve(self):
		csv_reader = csv.reader(open('data36.csv'))
		pass

if __name__ == '__main__':
    s = Solution()
    s.solve()
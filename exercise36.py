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

import numpy as np
from scipy.stats import chi2

class Solution():
	def solve(self):
		count_exp = [[154, 132], [180, 126], [104, 131]]
		count_the = np.ndarray((3, 2))
		total_r = [286, 306, 235]
		total_c = [438, 389]
		for i in range(3):
			for j in range(2):
				count_the[i][j] = total_r[i] * total_c[j] / 827.0
				print count_the[i][j]

		x2 = 0.0
		for i in range(3):
			for j in range(2):
				x2 = x2 + (count_exp[i][j] - count_the[i][j]) ** 2 / count_the[i][j]

		de = chi2.ppf(0.95, 5)
		print de
		print x2
		if x2 >= de:
			print [2, round(x2, 2), False]
			#测试用例给的统计量答案是11.47
			return [2, round(x2, 2), False]
		else:
			print [2, round(x2, 2), True]
			return [2, round(x2, 2), True]

if __name__ == '__main__':
	s = Solution()
	s.solve()
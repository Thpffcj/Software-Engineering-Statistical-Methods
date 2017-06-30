#-*- coding:utf-8 -*-
'''
New York is known as "the city that never sleeps". A random sample of 25 New Yorkers were asked how much sleep they get per night. Statistical summaries of these
data are shown below. Do these data provide strong evidence that New Yorkers sleep less than 8 hours per night on average?
Null-hypothesis is H0: u=8, and alpha is 0.05
n	mean	stand-variance	min	    max
25	7.73	    0.77	    6.17	9.78
Extra:
(1) If you were to construct a 90% confidence interval that corresponded to this hypothesis test, would you expect 8 hours to be in the interval? Explain your reasoning.

纽约被称为“不睡觉的城市”。 25名纽约客人的随机样本被问及每晚晚上多少睡眠。 这些数据的统计摘要如下。 这些数据是否提供了有力的证据表明，纽约人平均每晚睡眠时间少于8小时？
空假设为H0：u = 8，α为0.05
额外：
（1）如果你建立一个对应于这个假设检验的90％置信区间，你会期望8个小时在这个区间？ 解释你的推理。
'''

import numpy as np
from scipy.stats import t

class Solution():
	def solve(self):
		#Percent point function (inverse of cdf) at q of the given RV.累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
		de = t.ppf(0.95, 24)
		print de
		result = (7.73-8) /(0.77/np.sqrt(25))
		print result
		if result <= -de:
			print([24, round(result, 2), False])
			return [24, round(result, 2), False]
		else:
			print([24, round(result, 2), True])
			return [24, round(result, 2), True]

if __name__ == '__main__':
    s = Solution()
    s.solve()
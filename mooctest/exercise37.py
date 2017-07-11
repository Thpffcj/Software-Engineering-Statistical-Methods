#-*- coding:utf-8 -*-
'''
 Georgianna claims that in a small city renowned for its music school, the average child takes at least 5 years of piano lessons. We have a random sample
 of 20 children from the city with a mean of 4.6 years of piano lessons and a standard deviation of 2.2 years. Evaluate Georgianna's claims using a hypothesis
 test. alpha is 0.05.
Extra:
(1) Construct a 95% confidence interval for the number of years students in this city takes piano lessons and interpret it in context of the data.
(2) Do your results from the hypothesis test and the confidence interval agree? Explain your reasoning.

Georgianna声称，在以音乐学院而闻名的小城市中，平均每个孩子至少需要5年的钢琴课。 我们随机抽取20名城市儿童，平均4.6岁钢琴课，标准偏差为2.2岁。 使用假设检验评
估Georgianna的声明。 α为0.05。
额外：
（1）建立95％的置信区间，让这个城市的学生学习钢琴课，并在数据的背景下进行解释。
（2）从假设检验结果和置信区间是否一致？ 解释你的推理。

Output Description

[degree-of-freedom-of-distribution, statistical values, conclusion],'degree-of-freedom-of-distribution' and 'statistical values' are accurate to the second
decimal place, 'conclusion' is True, which means the H0 is accepted, or False
输出说明
[degree-of-freedom-of-distribution, statistical values, conclusion]
[分配度，统计值，结论]，“分配自由度”和“统计值”精确到第二位小数，“结论”为True，这意味着 H0被接受，或者是False
'''
import numpy as np
from scipy.stats import t

class Solution():
	def solve(self):
		average = 4.6
		s = 2.2
		de = t.ppf(0.975, 19)
		print de
		result = (average - 5) / (s / np.sqrt(20))
		if result <=  -de:
			print [round(19, 2), round(result, 2), False]
			return [round(19, 2), round(result, 2), False]
		else:
			print [round(19, 2), round(result, 2), True]
			return [round(19, 2), round(result, 2), True]


if __name__ == '__main__':
    s = Solution()
    s.solve()
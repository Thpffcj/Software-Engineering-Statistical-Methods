#-*- coding:utf-8 -*-
'''
A large farm wants to try out a new type of fertilizer to evaluate whether it will improve the farm's corn production. The land is broken into
plots that produce an average of 1.215 pounds of corn with a standard deviation of 94 pounds per plot. The owner is interested in detecting any
average difference of at least 40 pounds per plot. How many plots of land would be needed for the experiment if the desired power level is 90%?
Assume each plot of land gets treated with either the current fertilizer or the new fertilizer.

一个大农场想要尝试一种新型的肥料来评估是否会改善农场的玉米产量。 这片土地被平铺化，平均产量为1.215磅玉米，标准偏差为每磅94磅。 所有者有兴趣检测每个地
块至少40磅的平均差异。 如果所需功率水平为90％，则实验需要多少块土地？ 假设每一块土地都要用现在的肥料或新的肥料来处理。

Output Description
plot_num, int type
'''

from scipy.stats import norm
import numpy as np

class Solution():
	def solve(self):
		de = norm.ppf(0.975)
		print de

if __name__ == '__main__':
    s = Solution()
    s.solve()
#-*- coding:utf-8 -*-
'''
A 95% confidence interval for a population mean, u, is given as (18.985, 21.015). This confidence interval is based on a simple random
samples of 36 observations. Calculate the sample mean and standard deviation. Assume that all conditions necessary for inference are
satisfied. Use the t-distribution in any calculations.
人口平均值u的95％置信区间给出为（18.985,21.015）。 这个置信区间是基于一个简单的随机
样本36观察。 计算样品平均值和标准偏差。 假设推理所需的所有条件都是
满意。 在任何计算中使用t分布。
'''

from scipy import stats
import numpy as np

class Solution():
    def solve(self):
        t = stats.t(35)
        t1 = t.ppf(0.025)
        print t1
        n = 36
        x = round((18.985 + 21.015) / 2, 2)
        s = round(np.sqrt((21.015 - x) * np.sqrt(n) / t1), 2)
        list = [x, s]
        print list
        return list

if __name__ == '__main__':
    s = Solution()
    s.solve()
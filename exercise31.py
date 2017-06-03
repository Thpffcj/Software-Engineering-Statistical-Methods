#-*- coding:utf-8 -*-
'''
随着中国经济发展，人们生活质量相应提升，但睡眠质量却并不乐观。据《2016中国睡眠指数报告》显示，中国人平均睡眠时长为8.5小时，
这是从3600份问卷统计得到的结果。另外报告指出，中国人睡眠时长符合方差为25的正态分布，试写solve函数估计中国人睡眠时长的置信
区间(置信水平为95%)
'''
import math

class Solution:
    def solve(self):
        average = 8.5
        variance = 25
        n = 3600
        z = 1.96
        low = average - z * math.sqrt(variance) / math.sqrt(n)
        high = average + z * math.sqrt(variance) / math.sqrt(n)
        list = [low, high]
        return list

if __name__ == '__main__':
    s = Solution()

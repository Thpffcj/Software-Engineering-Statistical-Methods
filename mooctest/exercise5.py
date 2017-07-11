#-*- coding:utf-8 -*-
'''
Input Example
[23,45,76,67,17]
Input Description
一个含素数和非素数的多个整数列表
Output Example
[23,67,17]
Output Description
素数组成的列表
'''

class Solution():
	def solve(self, A):
		list = []
		for number in A:
			if(self.prime(number)):
				list.append(number)
		for number in list:
			print number
		return list

	#judge whether x is prime or not
	def prime(self, x):
		if(x == 2):
			return True
		num = 2
		while num<x:
			if(x%num == 0):
				return False
			num += 1
		return True

s = Solution()
s.solve([23,45,76,67,17])

#encoding = utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Perceptron(object):

	file = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
	df = pd.read_csv(file, header=None)

	y = df.loc[0:100, 4].values
	y = np.where(y == 'Iris-setosa', -1, 1)

	X = df.iloc[0:100, [0, 2]].values

	plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
	plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')

	plt.xlabel('花瓣长度')
	plt.ylabel('花径长度')
	plt.legend(loc='upper left')
	plt.show()
	# eta 学习率
	# n_iter权重向量的训练次数
	# w_ 神经元权重向量
	# errors_ 用于记录神经元判断出错次数
	def __int__(self, eta = 0.01, n_iter=10):
		self.eta = eta
		self.n_iter = n_iter
		pass

	def fit(self, X, y):
		# 输入训练数据，培训神经元，X输入样本向量，y对应样本分类
		# X shape[n_samples, n_features]
		# X[[1,2,3],[4,5,6]
		# n_samples=2， n_features=3
		# y [1,-1]
		# 初始化权重向量为0
		# 加一是因为前面算法提到的w0，也就是步调函数阈值
		self.w_ = np.zeros(1+X.shape[1])
		self.erros_ = []

		for _ in range(self.n_iter):
			errors = 0
			'''
			X [[1,2,3],[4,5,6]
			y [1,-1]
			zip(X,y) = [[1,2,3, 1],[4,5,6, -1]
			'''
			for xi, target in zip(X,y):
				# update = η * (y - y')
				update = self.eta * (target - self.predict(xi))
				# xi是一个向量
				# 权重更新
				self.w_[1:] += update * xi
				self.w_[0] += update
				errors += int(update != 0.0)
				self.erros_.append(errors)
				pass

		pass

	def net_input(self, X):
		# z = W0*1 + W1*X1 + W2*X2 + ...
		return np.dot(X, self.w_[1:]+self.w_[0])

	def predict(self, X):
		return np.where(self.net_input(X) >= 0.0 , 1, -1)
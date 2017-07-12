#encoding=utf-8
import numpy as np
import pandas as pd

def main():

	#预处理
	from sklearn.datasets import load_iris
	iris = load_iris()
#	print iris
	print len(iris["data"])
	from sklearn.cross_validation import train_test_split
	train_data,test_data,train_target,test_target = train_test_split(iris.data, iris.target, test_size=0.2,  random_state=1)

	#建模
	from sklearn import tree
	clf = tree.DecisionTreeClassifier(criterion="entropy")
	clf.fit(train_data, train_target)
	y_pred = clf.predict(test_data)

	#验证
	from sklearn import metrics
	print metrics.accuracy_score(y_true=test_target, y_pred=y_pred)
	print metrics.confusion_matrix(y_true=test_target, y_pred=y_pred)

if __name__=="__main__":
	main()
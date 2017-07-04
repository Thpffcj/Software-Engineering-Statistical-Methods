#encoding=utf-8
import numpy as np

def main():
	#积分
	from scipy.integrate import quad, dblquad, nquad
	print(quad(lambda x:np.exp(-x), 0, np.inf))
	print(dblquad(lambda t,x:np.exp(-x*t)/t**3, 0, np.inf, lambda x:1, lambda x:np.inf))
	def f(x, y):
		return x*y
	def bound_y():
		return [0, 0.5]
	def bound_x(y):
		return [0, 1-2*y]
	print(nquad(f, [bound_x, bound_y]))

if __name__ == '__main__':
    main()

import math
import numpy as np
from scipy import stats
#################################
#function for calculating the probability function for a univariate set and return its log
#function pf(x, mu, sigma)
#input : data element, mean and standard deviation
#output : log of probability distibution of x

def Upf(x, mu, sigma):
	# px=math.exp(-1*(((x-mu)/sigma)**2)/2)/math.sqrt(2*math.pi*sigma)
	val=stats.norm(mu,sigma).pdf(x)
	product=0;
	# print (val)
	for i in range(0,val.size):
		product=product+math.log(val[i])
	return product

#################################
#function for calculating the Multivariate form of probability function for a Multivariate set and return its log
#function Mpf(x, mu, covarianceMat)
#input : data set, mean vector and covraiance matrix
#output : sum of the logs of probability distibution of x

def Mpf(x, mu, covarianceMat):
	[m,n]=x.shape
	Sum=0
	for i in range(0,m):
		Mpx=math.exp(-1*((x[i,:]-mu).dot(np.linalg.inv(covarianceMat)).dot(np.transpose(x[i,:]-mu)))/2)/math.sqrt(((2*math.pi)**4)*np.linalg.det(covarianceMat))
	# print((x-mu).dot(np.linalg.inv(covarianceMat)).dot(np.transpose(x-mu)))
		Sum=math.log(Mpx)+Sum

	return Sum



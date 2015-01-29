from __future__ import division
import numpy.random
import math

num_train = 1555
num_test = 173
total = 1728
num_of_features = 6
bias_term = 0
alpha = 0.01
threshold = 0.01

def hypothesis(theta,x):
	sum = 0
	for i in range(len(theta)):
		sum += theta[i]*x[i]
	sum += bias_term
	return 1/(1+math.exp(-1*sum))

def two_norm_distance(v1,v2):
	sum = 0
	for i in range(len(v1)):
		sum += (v1[i]-v2[i])**2
	return math.sqrt(sum)

if __name__ == '__main__':

	testset = numpy.random.randint(total, size=num_test)+1
# 	testset = [ 665,1404,527,1605,401,73,1360,1431,170,1265,710,644,636,23,639\
# ,1363,194,1328,635,415,706,1547,1161,520,726,865,1215,840,338,835\
# ,768,601,1402,518,257,585,1668,1249,1471,594,885,221,1604,186,263\
# ,1010,1110,1411,383,695,945,1555,1028,1657,1657,1078,1348,707,825,1020\
# ,1365,989,729,552,362,1316,615,882,812,625,428,1340,596,1118,345\
# ,975,503,167,912,478,1224,452,647,149,1447,966,1172,952,83,1383\
# ,804,148,881,1250,103,155,54,697,7,1079,1243,1486,1163,297,516\
# ,890,560,733,1008,823,216,1256,460,1495,1686,38,1406,1534,1358,999\
# ,527,130,1168,1116,1018,180,139,555,874,1407,1396,1574,653,638,824\
# ,1183,1213,170,1111,966,1417,779,1169,1477,860,1087,543,74,160,1680\
# ,648,571,416,1433,973,1415,1056,805,1563,1141,621,536,347,368,261\
# ,1036,790,464,968,519,374,1351,990]

	# print testset

	theta = numpy.random.random_sample(num_of_features)
	# theta = [-0.53398006,-0.24628524,-0.60147105,-0.19029636,-0.47225776,-0.42588647]
	# theta = [0.53398006,0.24628524,0.60147105,0.19029636,0.47225776,0.42588647]
	# print theta

	# print theta
	y = 0
	x = [1]*(num_of_features)


	f = open('remappered.data')
	while True:
		old = theta[:]
		f.seek(0)
		count = 1
		for line in f:
			# print theta
			words = line.split(',')
			if count not in testset:
				if words[6].strip('\n')=='1':
					y = 0
				else:
					y = 1

				for i in range(0,num_of_features):
					x[i] = float(words[i])
				
				for i in range(0,num_of_features):
					theta[i] = theta[i] + alpha*(y-hypothesis(theta,x))*x[i]

			count += 1

		if two_norm_distance(old,theta) < threshold:
			break

	# print theta


	res = 0
	count = 1
	f.seek(0)
	for line in f:
		words = line.split(',')
		if count in testset:
			if words[6].strip('\n')=='1':
				y = 0
			else:
				# print words[6].strip('\n')
				y = 1

			for i in range(0,num_of_features):
				x[i] = float(words[i])

			if hypothesis(theta,x) >= 0.5:
				# print hypothesis(theta,x)
				predict = 1
			else:
				predict = 0

			if predict == y:
				res += 1

		count += 1
	print res
	print res/num_test





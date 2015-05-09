import random
import math

num_sample = 5000
fp = open("rejection_samples.txt","w")

A = [0.8,0.2]
B = [[0.9,0.1],[0.8,0.2]]
C = [[[1,0],[0.8,0.2]],[[0.99,0.01],[0.5,0.5]]]

#X[0],X[1],X[2]---> A,B,C

rate_set = []

for t in range(10):

	rejected = 0

	X = [0]*3
	i = 0

	while i < 5000:

		X[0] = 0 if random.random() < A[0] else 1
		X[1] = 0 if random.random() < B[X[0]][0] else 1
		X[2] = 0 if random.random() < C[X[0]][X[1]][0] else 1
		if X[2] == 1:
			i = i + 1
			fp.write(str(X).strip('[]')+'\n')
		else:
			rejected = rejected + 1

	rate_set.append(rejected/float(rejected+5000))
	print "{}:{}".format(t,rejected/float(rejected+5000))


mean = sum(rate_set)/float(10)
var = 0
for i in range(10):
	var += (rate_set[i]-mean)**2
var = var/float(10)
std = math.sqrt(var)
SEM = std/math.sqrt(10)

print "[{},{}]".format(-1.96*SEM+mean,1.96*SEM+mean)




	





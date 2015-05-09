import random
import math

num_sample = 5000
fp = open("lw_samples.txt","w")

A = [0.8,0.2]
B = [[0.9,0.1],[0.8,0.2]]
C = [[[1,0],[0.8,0.2]],[[0.99,0.01],[0.5,0.5]]]

mean_set = []

for t in range(10):
	W = {}

	A1 = 0;
	B1 = 0;
	total = 0;

	#X[0],X[1],X[2]---> A,B,C

	X = [0]*3

	for i in range(5000):
		w = 1
		X[0] = 0 if random.random() < A[0] else 1
		X[1] = 0 if random.random() < B[X[0]][0] else 1
		X[2] = 1
		w = w * C[X[0]][X[1]][1]

		A1 += w if X[0] == 1 else 0
		B1 += w if X[1] == 1 else 0
		total += w

		if w in W:
			W.update({w:W[w]+1})
		else:
			W[w] = 1

		fp.write(str(w)+','+str(X).strip('[]')+'\n')


	# print W

	mean = 0

	for k in W:
		mean += k*W[k]

	mean /= float(5000)
	# print mean
	mean_set.append(mean)
	print "{}:{}".format(t,mean)


mean_of_mean = sum(mean_set)/float(10)
var = 0
for i in range(10):
	var += (mean_set[i]-mean_of_mean)**2
var = var/float(10)
std = math.sqrt(var)
SEM = std/math.sqrt(10)

print "[{},{}]".format(-1.96*SEM+mean_of_mean,1.96*SEM+mean_of_mean)



print "P(A=1|C=1)={0}".format(A1/total)
print "P(B=1|C=1)={0}".format(B1/total)








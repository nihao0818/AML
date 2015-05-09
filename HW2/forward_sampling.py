import random

num_sample = 5000
fp = open("forward_samples.txt","w")

A = [0.8,0.2]
B = [[0.9,0.1],[0.8,0.2]]
C = [[[1,0],[0.8,0.2]],[[0.99,0.01],[0.5,0.5]]]

#X[0],X[1],X[2]---> A,B,C

X = [0]*3

for i in range(5000):

	X[0] = 0 if random.random() < A[0] else 1
	X[1] = 0 if random.random() < B[X[0]][0] else 1
	X[2] = 0 if random.random() < C[X[0]][X[1]][0] else 1

	# print str(X).strip('[]')

	fp.write(str(X).strip('[]')+'\n')




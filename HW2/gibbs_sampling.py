import random

num_sample = 5000
fp = open("gibbs_samples.txt","w")

A = [0.8,0.2]
B = [[0.9,0.1],[0.8,0.2]]
C = [[[1,0],[0.8,0.2]],[[0.99,0.01],[0.5,0.5]]]

#X[0],X[1],X[2]---> A,B,C

cA = 0
cB = 0

X = [0]*3
X[2] = 1

i = 0

while i < 5100:

	# A[1]*B[1][X[1]]*C[1][X[1]][1]/float(A[1]*B[1][X[1]]*C[1][X[1]][1]+A[0]*B[0][X[1]]*C[0][X[1]][1])
	# B[X[0]][1]*C[X[0]][1][1]/float(B[X[0]][1]*C[X[0]][1][1]+B[X[0]][0]*C[X[0]][0][1])

	X[0] = 1 if random.random() < A[1]*B[1][X[1]]*C[1][X[1]][1]/float(A[1]*B[1][X[1]]*C[1][X[1]][1]+A[0]*B[0][X[1]]*C[0][X[1]][1]) else 0
	X[1] = 1 if random.random() < 	B[X[0]][1]*C[X[0]][1][1]/float(B[X[0]][1]*C[X[0]][1][1]+B[X[0]][0]*C[X[0]][0][1]) else 0



	if i >= 100:

		if X[0] == 1:
			cA += 1
		if X[1] == 1:
			cB += 1

		fp.write(str(X).strip('[]')+'\n')



	i += 1


print "P(a=1 | c=1) = {}".format(cA/float(num_sample)) 
print "P(b=1 | c=1) = {}".format(cB/float(num_sample)) 




	





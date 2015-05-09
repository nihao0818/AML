import random

num_sample = 5000
fp = open("forward_samples.txt")

A = 0
B = 0
C = 0

#X[0],X[1],X[2]---> A,B,C

X = [0]*3

for line in fp:
	line_content = line.split(",")
	A = A + 1 if line_content[0].strip(' \n') == '1' else A
	B = B + 1 if line_content[1].strip(' \n') == '1' else B
	C = C + 1 if line_content[2].strip(' \n') == '1' else C

print "P(a=1) = {0}".format(A/float(num_sample))
print "P(b=1) = {0}".format(B/float(num_sample))
print "P(c=1) = {0}".format(C/float(num_sample))


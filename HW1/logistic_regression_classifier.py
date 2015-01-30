from __future__ import division
import numpy.random
import math

num_train = 1555
num_test = 173
total = 1728
num_of_features = 6
alpha = 0.01
threshold = 0.01

#calculate h()
def hypothesis(theta,x):
	sum = 0
	for i in range(len(theta)):
		sum += theta[i]*x[i]
	return 1/(1+math.exp(-1*sum))

#calculate the 2-norm distance between two vectors
def two_norm_distance(v1,v2):
	sum = 0
	for i in range(len(v1)):
		sum += (v1[i]-v2[i])**2
	return math.sqrt(sum)

if __name__ == '__main__':

	#generate a random list which specifies the test set
	testset = numpy.random.randint(total, size=num_test)+1

	#generate the initial weights
	theta = numpy.random.random_sample(num_of_features+1)*-1
	#theta[0] is the bias term

	y = 0
	x = [1]*(num_of_features+1)

	# trainning
	f = open('remappered.data')
	while True:
		old = list(theta)
		f.seek(0)
		count = 1
		mysum = [0]*7
		for line in f:
			words = line.split(',')

			#if this line of data is choosen as train set
			if count not in testset:
				#get y by mapping the tag from -1,1 to 0,1
				if words[6].strip('\n')=='1':
					y = 0
				else:
					y = 1
				#get vector x
				for i in range(1,num_of_features+1):
					x[i] = float(words[i])
				#calculate the error
				for i in range(0,num_of_features+1):
					mysum[i] = mysum[i] + alpha*(y-hypothesis(theta,x))*x[i]
			count += 1
		#update theta(weights)					
		for i in range(0,num_of_features+1):
			theta[i] += alpha*mysum[i] 
		
		#check if reaching the threshold 
		if two_norm_distance(old,theta) < threshold:
			break




	#testing
	res = 0
	count = 1
	f.seek(0)
	for line in f:
		words = line.split(',')
		if count in testset:
			if words[6].strip('\n')=='1':
				y = 0
			else:
				y = 1

			for i in range(1,num_of_features+1):
				x[i] = float(words[i])

			if hypothesis(theta,x) >= 0.5:
				predict = 1
			else:
				predict = 0

			if predict == y:
				res += 1

		count += 1
	# print res
	print res/num_test







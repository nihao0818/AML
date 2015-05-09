import numpy as np
import random
import math
import matplotlib.pyplot as plt



num_train = 1209
num_test = 519
total = 1728
step = 1000

train_data=[]
test_data=[]

train_error=[]
test_error=[]


D=[1/float(num_train)]*num_train

def NaiveBayesianClassifier(data,D):
	total = len(data)

	buying = [[0,0,0,0],[0,0,0,0]]
	maint = [[0,0,0,0],[0,0,0,0]]
	doors = [[0,0,0,0],[0,0,0,0]]
	persons = [[0,0,0],[0,0,0]]
	lug_boot = [[0,0,0],[0,0,0]]
	safety = [[0,0,0],[0,0,0]]
	negtotal = 0
	postotal = 0

	index = 0
	for line in data:
		if line[1] == -1:
			buying[0][line[0][0]-1] += D[index]
			maint[0][line[0][1]-1] += D[index]
			doors[0][line[0][2]-1] += D[index]
			persons[0][line[0][3]-1] += D[index]
			lug_boot[0][line[0][4]-1] += D[index]
			safety[0][line[0][5]-1] += D[index]
			negtotal += D[index]
		else:
			buying[1][line[0][0]-1] += D[index]
			maint[1][line[0][1]-1] += D[index]
			doors[1][line[0][2]-1] += D[index]
			persons[1][line[0][3]-1] += D[index]
			lug_boot[1][line[0][4]-1] += D[index]
			safety[1][line[0][5]-1] += D[index]
			postotal += D[index]
		index += 1

	for n in range(2):
		buying[n] = [i/float(sum(buying[n])) for i in buying[n]]
		maint[n] = [i/float(sum(maint[n])) for i in maint[n]]
		doors[n] = [i/float(sum(doors[n])) for i in doors[n]]
		persons[n] = [i/float(sum(persons[n])) for i in persons[n]]
		lug_boot[n] = [i/float(sum(lug_boot[n])) for i in lug_boot[n]]
		safety[n] = [i/float(sum(safety[n])) for i in safety[n]]



	negtotal = negtotal/float(negtotal+postotal)
	postotal = postotal/float(negtotal+postotal)

	return [buying,maint,doors,persons,lug_boot,safety,negtotal,postotal]



#create training set
testset = random.sample(range(1,total+1),num_test)

f = open('remappered.data')
count = 1
for line in f:
	words = line.split(',')
	if count not in testset:
		train_data.append([  [int(i) for i in words[:-1]] ,  int(words[-1:][0].strip('\n'))  ])
	else:
		test_data.append([  [int(i) for i in words[:-1]] ,  int(words[-1:][0].strip('\n'))  ])
	count += 1



#train strong classifier
strong_classifier = []
for t in range(step):

	weak_classifier = NaiveBayesianClassifier(train_data,D)

	error = 0
	index = 0
	y_h = []
	count = 0

	for line in train_data:
		y=line[1]
		neg = weak_classifier[0][0][line[0][0]-1]\
		*weak_classifier[1][0][line[0][1]-1]\
		*weak_classifier[2][0][line[0][2]-1]\
		*weak_classifier[3][0][line[0][3]-1]\
		*weak_classifier[4][0][line[0][4]-1]\
		*weak_classifier[5][0][line[0][5]-1]\
		*weak_classifier[6]
		pos = weak_classifier[0][1][line[0][0]-1]\
		*weak_classifier[1][1][line[0][1]-1]\
		*weak_classifier[2][1][line[0][2]-1]\
		*weak_classifier[3][1][line[0][3]-1]\
		*weak_classifier[4][1][line[0][4]-1]\
		*weak_classifier[5][1][line[0][5]-1]\
		*weak_classifier[7]

		predict = 0
		if neg > pos:
			predict = -1
		else:
			predict = 1
		if predict != y:
			error += D[index]				
			count += 1

		y_h.append([y,predict,index])			
		index += 1

	# error = count/float(num_train)
	# error = 1/float(count)
	# print error
	train_error.append(error)

	a = 0.5*np.log((1-error)/float(error))

	record = []
	for i in y_h:
		if i[2] not in record:
			D[i[2]] = D[i[2]]*math.exp(-a*i[0]*i[1])
			record.append(i[2])

	Z=sum(D)
	for i in range(num_train):
		D[i] = D[i]/float(Z)

	strong_classifier.append([a,weak_classifier])


#calulate test error
hit = [0]*step
false_positive = [0]*step
true_positive = [0]*step
false_negative = [0]*step
true_negative = [0]*step

for line in test_data:
	y=line[1]
	before_sign = [0]*step
	index = 0
	# print line[0]

	for i in strong_classifier:
		weak_classifier = i[1]
		# print i[0]
		neg = weak_classifier[0][0][line[0][0]-1]\
		*weak_classifier[1][0][line[0][1]-1]\
		*weak_classifier[2][0][line[0][2]-1]\
		*weak_classifier[3][0][line[0][3]-1]\
		*weak_classifier[4][0][line[0][4]-1]\
		*weak_classifier[5][0][line[0][5]-1]\
		*weak_classifier[6]
		pos = weak_classifier[0][1][line[0][0]-1]\
		*weak_classifier[1][1][line[0][1]-1]\
		*weak_classifier[2][1][line[0][2]-1]\
		*weak_classifier[3][1][line[0][3]-1]\
		*weak_classifier[4][1][line[0][4]-1]\
		*weak_classifier[5][1][line[0][5]-1]\
		*weak_classifier[7]

		predict = 0
		if neg > pos:
			predict = -1
		else:
			predict = 1

		if index == 0:
			before_sign[index] = i[0]*predict
		else:
			before_sign[index] = before_sign[index-1] + i[0]*predict

		index += 1
	for i in range(step):
		after_sign = -1 if before_sign[i] < 0 else 1 
		hit[i] += 1 if after_sign == y else 0
		false_positive[i] += 1 if after_sign == 1 and y==-1 else 0
		true_positive[i] += 1 if after_sign == 1 and y==1 else 0
		false_negative[i] += 1 if after_sign == -1 and y==1 else 0
		true_negative[i] += 1 if after_sign == -1 and y==-1 else 0


test_error = [(num_test-i)/float(num_test) for i in hit]
false_positive_rate = [false_positive[i]/float(false_positive[i]+true_negative[i]) for i in range(step)]
false_negative_rate = [false_negative[i]/float(false_negative[i]+true_positive[i]) for i in range(step)]


print hit[step-1]/float(num_test)

print "Adaboost_NB error rate is: {}".format((num_test-hit[step-1])/float(num_test))
print "Adaboost_NB false positive rate is: {}".format(false_positive[step-1]/float(false_positive[step-1]+true_negative[step-1]))
print "Adaboost_NB false negative rate is: {}".format(false_negative[step-1]/float(false_negative[step-1]+true_positive[step-1]))

display_scope = 1000


# t = range(1,display_scope+1)

# plt.figure(1)
# ax = plt.subplot(211)
# ax.set_title("train_error")
# ax.plot(t, train_error[:display_scope])

# plt.suptitle('Error vs. Iterations')

# ax = plt.subplot(212)
# ax.set_title("test_error")
# ax.plot(t, test_error[:display_scope])

# plt.show()


# t = range(1,display_scope+1)

# plt.figure(1)
# ax = plt.subplot(211)
# ax.set_title("false_positive_rate")
# ax.plot(t, false_positive_rate[:display_scope])

# plt.suptitle('false_positive vs. false_negative')

# ax = plt.subplot(212)
# ax.set_title("false_negative_rate")
# ax.plot(t, false_negative_rate[:display_scope])

# plt.show()

D=[1/float(num_train)]*num_train

weak_classifier = NaiveBayesianClassifier(train_data,D)
hit = 0
false_positive = 0
true_positive = 0
false_negative = 0
true_negative = 0

for line in test_data:
	y=line[1]

	neg = weak_classifier[0][0][line[0][0]-1]\
	*weak_classifier[1][0][line[0][1]-1]\
	*weak_classifier[2][0][line[0][2]-1]\
	*weak_classifier[3][0][line[0][3]-1]\
	*weak_classifier[4][0][line[0][4]-1]\
	*weak_classifier[5][0][line[0][5]-1]\
	*weak_classifier[6]
	pos = weak_classifier[0][1][line[0][0]-1]\
	*weak_classifier[1][1][line[0][1]-1]\
	*weak_classifier[2][1][line[0][2]-1]\
	*weak_classifier[3][1][line[0][3]-1]\
	*weak_classifier[4][1][line[0][4]-1]\
	*weak_classifier[5][1][line[0][5]-1]\
	*weak_classifier[7]

	predict = 0
	if neg > pos:
		predict = -1
	else:
		predict = 1

	hit += 1 if predict == y else 0
	false_positive += 1 if predict == 1 and y==-1 else 0
	true_positive += 1 if predict == 1 and y==1 else 0
	false_negative += 1 if predict == -1 and y==1 else 0
	true_negative += 1 if predict == -1 and y==-1 else 0



print "NB error rate is: {}".format((num_test-hit)/float(num_test))
print "NB false positive rate is: {}".format(false_positive/float(false_positive+true_negative))
print "NB false negative rate is: {}".format(false_negative/float(false_negative+true_positive))




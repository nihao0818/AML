from sklearn.cross_validation import cross_val_score
from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier
import numpy as np
import random
import math

num_train = 1209
num_test = 519
total = 1728
step = 1000

train_data=[]
test_data=[]

train_error=[]
test_error=[]

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

data = []
target = []

for row in train_data:
	data.append(row[0])
	target.append(row[1])

clf = AdaBoostClassifier(n_estimators=2)

scores = cross_val_score(clf, data, target)
print scores.mean()    
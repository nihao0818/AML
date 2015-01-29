from __future__ import division
import numpy.random


num_train = 1555
num_test = 173
total = 1728

if __name__ == '__main__':
	buying = [[0]*4]*2
	maint = [[0]*4]*2
	doors = [[0]*4]*2
	persons = [[0]*3]*2
	lug_boot = [[0]*3]*2
	safety = [[0]*3]*2

	testset = numpy.random.randint(total, size=num_test)+1

	negtotal = 0
	postotal = 0

	res = 0

	f = open('remappered.data')
	count = 1
	for line in f:
		words = line.split(',')
		if count not in testset:
			if words[6].strip('\n') == '-1':
				buying[0][int(words[0])-1] += 1
				maint[0][int(words[1])-1] += 1
				doors[0][int(words[2])-1] += 1
				persons[0][int(words[3])-1] += 1
				lug_boot[0][int(words[4])-1] += 1
				safety[0][int(words[5])-1] += 1
				negtotal += 1
			else:
				buying[1][int(words[0])-1] += 1
				maint[1][int(words[1])-1] += 1
				doors[1][int(words[2])-1] += 1
				persons[1][int(words[3])-1] += 1
				lug_boot[1][int(words[4])-1] += 1
				safety[1][int(words[5])-1] += 1
				postotal += 1
		count += 1

	res = 0
	count = 1
	f.seek(0)
	for line in f:
		words = line.split(',')
		if count in testset:
			neg = buying[0][int(words[0])-1]/(buying[0][0] + buying[0][1] + buying[0][2] + buying[0][3])\
			*maint[0][int(words[1])-1]/(maint[0][0] + maint[0][1] + maint[0][2] + maint[0][3])\
			*doors[0][int(words[2])-1]/(doors[0][0] + doors[0][1] + doors[0][2] + doors[0][3])\
			*persons[0][int(words[3])-1]/(persons[0][0] + persons[0][1] + persons[0][2])\
			*lug_boot[0][int(words[4])-1]/(lug_boot[0][0] + lug_boot[0][1] + lug_boot[0][2])\
			*safety[0][int(words[5])-1]/(safety[0][0] + safety[0][1] + safety[0][2])\
			*negtotal/num_train

			pos = buying[1][int(words[0])-1]/(buying[1][0] + buying[1][1] + buying[1][2] + buying[1][3])\
			*maint[1][int(words[1])-1]/(maint[1][0] + maint[1][1] + maint[1][2] + maint[1][3])\
			*doors[1][int(words[2])-1]/(doors[1][0] + doors[1][1] + doors[1][2] + doors[1][3])\
			*persons[1][int(words[3])-1]/(persons[1][0] + persons[1][1] + persons[1][2])\
			*lug_boot[1][int(words[4])-1]/(lug_boot[1][0] + lug_boot[1][1] + lug_boot[1][2])\
			*safety[1][int(words[5])-1]/(safety[1][0] + safety[1][1] + safety[1][2])\
			*postotal/num_train

			predict = ''
			if neg > pos:
				predict = '-1'
			else:
				predict = '1'
			if predict == words[6].strip('\n'):
				res += 1
		count += 1
	print res
	print res/num_test





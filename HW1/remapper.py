import sys


if __name__ == '__main__':
	inputfilename = sys.argv[1]
	outputfilename = sys.argv[2]

	buying = {'low':'1','med':'2','high':'3','vhigh':'4'}
	maint = {'low':'1','med':'2','high':'3','vhigh':'4'}
	doors = {'2':'1','3':'2','4':'3','5more':'4'}
	persons = {'2':'1','4':'2','more':'3'}
	lug_boot = {'small':'1','med':'2','big':'3'}
	safety = {'low':'1','med':'2','high':'3'}
	classDic = {'unacc':'-1','acc':'1','good':'1','vgood':'1'}
	f = open(inputfilename)
	f2 = open(outputfilename,'w+')

	class_minus_one = 0;
	class_one = 0;

	# while True:
	# for i in range(10):
	for line in f:
		# line = f.readline()
		# if not line:
		# 	break

		words = line.split(',')
		# print words
		f2.write(buying[words[0]]+',')
		f2.write(maint[words[1]]+',')
		f2.write(doors[words[2]]+',')
		f2.write(persons[words[3]]+',')
		f2.write(lug_boot[words[4]]+',')
		f2.write(safety[words[5]]+',')
		f2.write(classDic[words[6].strip('\n')])
		# print words[6].strip('\n')
		if classDic[words[6].strip('\n')] == '-1':
			class_minus_one += 1
		else:
			class_one += 1;

		f2.write('\n')

	print str(class_minus_one) + ' examples are class -1, while ' + str(class_one) + ' examples are class 1.'


	f.close()
	f2.close()

		


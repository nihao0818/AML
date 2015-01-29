import math

if __name__ == '__main__':
	f = open('lr_sample.data')
	v = []
	sum = 0
	for i in f:
		sum += float(i)
		v.append(float(i))
	mean = sum/10
	print mean
	sum = 0
	for i in v:
		sum += (i-mean)**2

	sum /= 10
	SD = math.sqrt(sum)
	SEM = SD/math.sqrt(10)
	print SEM

	print "[{},{}]".format(-1.96*SEM+mean,1.96*SEM+mean)
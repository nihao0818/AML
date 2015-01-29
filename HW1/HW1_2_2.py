import random
import sys

if __name__ == "__main__":
	times = int(sys.argv[1])
	sum = 0
	for i in range(times):
		t = random.randint(0,1)
		print t,
		sum += t
	print
	print sum
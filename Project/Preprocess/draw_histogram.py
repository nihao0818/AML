import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import sys

from numpy.random import normal



if __name__ == "__main__":
	filename = sys.argv[1]
	f = open(filename)
	freq = []
	ids = []
	for row in f:
		pair = row.strip('\n').split(',')
		ids.append(pair[0])
		freq.append(int(pair[1]))


	left = range(len(freq))
	# print left
	height = freq
	# left = 9
	# print len(height)
	# print height

	plt.bar(left, height)
	# plt.yticks(y_pos, people)
	plt.xlabel('Performance')
	plt.title('How fast do you want to go today?')

	plt.show()


	# plt.xlabel('Frequence')
	# plt.title(filename)


import numpy as np
import sys

from numpy.random import normal






if __name__ == "__main__":

	total = {}
	f_w = open("url_domain_map","w")
	f = open('train_play.output')

	for line in f:
		line_list = line.split()
		if line_list[2] == 'Q':	
			for pair in line_list[6:]:
				url = pair.strip('\n').split(",")[0]
				if url not in total:
					f_w.write(pair+'\n')
					total[url] = 1

	f.close()

	f_w.close()








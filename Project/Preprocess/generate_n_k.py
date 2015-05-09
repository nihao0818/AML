import numpy as np
import sys

from numpy.random import normal




if __name__ == "__main__":
	N = int(sys.argv[1])	#domain
	K = int(sys.argv[2]) #term
	terms = {}
	domains = {}
	domains2 = {}
	dataset = [[0 for i in range(K)] for j in range(N)]
	domain_id_click = [0 for i in range(N)]
	domain_id_appear = [0 for i in range(N)]
	total_term = [0 for i in range(K)]


	f_t = open("term_id_distribution_desc.txt")
	f_d = open("domain_id_distribution_desc.txt")

	for index in range(K):
		line = f_t.readline()
		# print line.split(',')[0]
		terms[line.split(',')[0]]=index

	for index in range(N):
		line = f_d.readline()
		domains[line.split(',')[0]]=index
		domains2[index] = line.split(',')[0]


	# print terms
	f_t.close()
	f_d.close()

	url_domain_map = {}
	f_m = open('url_domain_map_simplified')
	for line in f_m:
		line_list = line.strip('\n').split(',')
		if line_list[1] in domains:
			url_domain_map[line_list[0]] = line_list[1]
	f_m.close()


	f = open('train_play.output')
	for line in f:
		line_list = line.split()
		if line_list[2] == 'Q':	
			term_list = line_list[5].split(",")
	
			for pair in line_list[6:]:
				domain_id = pair.strip('\n').split(",")[1]
				if domain_id in domains:
					domain_id_appear[domains[domain_id]]+=1
					for term_id in term_list:
						if term_id in terms:
							total_term[terms[term_id]] += 1
							dataset[domains[domain_id]][terms[term_id]] += 1
		if line_list[2] == 'C':	
			url = line_list[4].strip('\n')
			if url in url_domain_map:
				domain_id_click[domains[url_domain_map[url]]] += 1



	f.close()

	data_matrix_file = "data_matrix_{0}_{1}.txt".format(N,K)
	# feature_weight_file = "feature_weight_{0}_{1}.txt".format(N,K)
	domain_id_click_over_appear_file = "domain_id_click_over_appear_{0}_{1}.txt".format(N,K)


	f_f = open(data_matrix_file,"w")
	for i in dataset:
		for e in range(K):
			if total_term[e] != 0:
				i[e] = i[e]/float(total_term[e])
			else:
				i[e] = 0
		f_f.write(','.join(map(str,i))+'\n')

	f_f_2 = open(domain_id_click_over_appear_file,"w")
	for i in range(N):
		if domain_id_appear[i] != 0:
			f_f_2.write(str(domains2[i])+','+str((domain_id_click[i])/float(domain_id_appear[i]))+'\n')
		else:
			f_f_2.write(str(domains2[i])+','+'0'+'\n')


	f_f.close()
	f_f_2.close()








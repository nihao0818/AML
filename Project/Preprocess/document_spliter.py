import sys

original_file = sys.argv[1]


if __name__ == "__main__":
	f = open(original_file)
	sub_files_term_id=[]
	sub_files_domain_id=[]
	for i in range(40):
		sub_files_term_id.append(open("./sub_files_term_id/"+str(i),"w"))
		sub_files_domain_id.append(open("./sub_files_domain_id/"+str(i),"w"))

	for line in f:
		line_list = line.split()
		if len(line_list) > 5:
			term_list = line_list[5].split(",")
			for term_id in term_list:
				# sub_files_term_id[int(term_id)%40].write(str(term_list)+'\n')

				sub_files_term_id[int(term_id)%40].write(term_id+'\n')
			for pair in line_list[6:]:
				domain_id = pair.strip('\n').split(",")[1]
				sub_files_domain_id[int(domain_id)%40].write(domain_id+'\n')

















	for i in range(40):
		sub_files_term_id[i].close()
		sub_files_domain_id[i].close()
	f.close()
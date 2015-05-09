import sys
from os import listdir


if __name__ == "__main__":

	unique_term = 0
	files = listdir('./result_files_term_id')[1:]
	for f in files:
		cur_file = open('./result_files_term_id/'+f)
		for row in cur_file:
			unique_term += 1
		cur_file.close()
		unique_term -= 1

	unique_domain = 0
	files = listdir('./result_files_domain_id')[1:]
	for f in files:
		cur_file = open('./result_files_domain_id/'+f)
		for row in cur_file:
			unique_domain += 1
		cur_file.close()
		unique_domain -= 1


	print "unique_term: {}".format(unique_term)	
	print "unique_domain: {}".format(unique_domain)
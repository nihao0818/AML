import sys
from os import listdir


# original_file = sys.argv[1]

result_files_term_id=[]
for i in range(40):
	result_files_term_id.append(open("./result_files_term_id/"+str(i),"w"))

if __name__ == "__main__":
	files = listdir('./sub_files_term_id')[1:]
	for f in files:
		cur_file = open('./sub_files_term_id/'+f)
		cur_dict = {}
		for line in cur_file:
			if line != "":
				term_id = line.strip('\n')
				if term_id in cur_dict:
					cur_dict[term_id] += 1
				else:
					cur_dict[term_id] = 1
		for key in cur_dict:
			result_files_term_id[int(f)].write(key+','+str(cur_dict[key])+'\n')

		cur_file.close()

for i in range(40):
	result_files_term_id[i].close()
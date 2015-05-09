import sys
from os import listdir


# original_file = sys.argv[1]

result_files_domain_id=[]
for i in range(40):
	result_files_domain_id.append(open("./result_files_domain_id/"+str(i),"w"))

if __name__ == "__main__":
	files = listdir('./sub_files_domain_id')[1:]
	for f in files:
		cur_file = open('./sub_files_domain_id/'+f)
		cur_dict = {}
		for line in cur_file:
			if line != "":
				domain_id = line.strip('\n')
				if domain_id in cur_dict:
					cur_dict[domain_id] += 1
				else:
					cur_dict[domain_id] = 1
		for key in cur_dict:
			result_files_domain_id[int(f)].write(key+','+str(cur_dict[key])+'\n')

		cur_file.close()

for i in range(40):
	result_files_domain_id[i].close()
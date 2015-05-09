import sys
from os import listdir
import heapq



if __name__ == "__main__":

	if sys.argv[1] == "term":
		heap = [] 
		files = listdir('./result_files_term_id')[1:]
		for f in files:
			cur_file = open('./result_files_term_id/'+f)
			for row in cur_file:
				if row != "":
					pair = row.strip('\n').split(",")
					if len(heap) < 10**6:
						heapq.heappush(heap, (int(pair[1]),pair[0]))
					else:
						heapq.heappushpop(heap, (int(pair[1]),pair[0]))
			cur_file.close()
		output_file = open("term_id_distribution.txt","w")
		heap.sort()
		for i in heap:
			output_file.write(i[1]+','+str(i[0])+'\n')


	else:

		heap = [] 
		files = listdir('./result_files_domain_id')[1:]
		for f in files:
			cur_file = open('./result_files_domain_id/'+f)
			for row in cur_file:
				if row != "":
					pair = row.strip('\n').split(",")
					if len(heap) < 10**6:
						heapq.heappush(heap, (int(pair[1]),pair[0]))
					else:
						heapq.heappushpop(heap, (int(pair[1]),pair[0]))
			cur_file.close()
		output_file = open("domain_id_distribution.txt","w")
		heap.sort()
		for i in heap:
			output_file.write(i[1]+','+str(i[0])+'\n')
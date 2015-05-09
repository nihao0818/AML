fp = open("cup98LRN.txt")
feature_dict = {}
size_of_feature = 0

head = fp.readline()

head = head.split(",")

size_of_head = len(head)

for i in range(size_of_head):
	feature_dict[head[i]] = []

line = fp.readline()
while line != "":
	line = line.split(",")
	for i in range(size_of_head):	
		feature_dict[head[i]].append(line[i])
	line = fp.readline()

while 1:
	feature = raw_input('Enter a feature name: ')
	print set(feature_dict[feature])



# print size_of_head,size_of_content

# print feature_dict["MDMAUD"]


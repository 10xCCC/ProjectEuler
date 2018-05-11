#! python3

def main():

	f = open("problem18_triangle.txt","r")
	
	triangle_list = []
	for line in f:
		line = [int(s) for s in line.split(' ')]
		triangle_list.append(line)

	list_to_merge = [0]*len(triangle_list[-1])
	# print(list_to_merge)
	while len(triangle_list) > 0:

		print("iteration number", len(triangle_list))
		
		last_list = triangle_list.pop()
		# print("last list is", last_list)
		
		for i in range(len(last_list)-1):
			last_list[i] = max(last_list[i],last_list[i + 1])
		
		# print(len(last_list))
		# print(len(last_list), len(list_to_merge))
		
		print("modified last_list is", last_list)
		# print(list_to_merge)

		
		for i in range(len(last_list)):
			list_to_merge[i] += last_list[i]
		print("max sums", list_to_merge)
		
		# break
		last_list.pop()
		list_to_merge.pop()
		# print(len(list_to_merge), len(last_list))
		print("max sums", list_to_merge)
		
		# break
	# print(triangle_list)


main()
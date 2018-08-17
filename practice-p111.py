table_data = [['apples','oranges','cherries','banana'],
			  ['Alice','Bob','Carol','David'],
			  ['dogs','cats','moose','goose']]

def get_length(table):
	length = []
	item_len = []
	for i in range(len(table)):
		# print(i)
		for k in range(len(table[i])):
			l = len(table[i][k])
			# print(table[i][k])
			item_len.append(l)
			# print(item_len)
		length.append(max(item_len))  #获取字符长度列表最大值
		item_len.clear()			  #清空字符长度列表

	def printTable(table):
		for x in range(len(table)+1):
			for y in range(len(table[0])-1):
				# print('x:' + str(x))
				# print('y:' + str(y))
				print(table[y][x].rjust(length[y],' '),end = ' | ')	
			print('\n')

	printTable(table)
# printTable(table_data)
get_length(table_data)
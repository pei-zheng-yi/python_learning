# spam = ['apple','bananas','tofu','cats','picth']
# for i in spam[:-1]:
# 	print(i + ',',end = '')
# print('and ' + spam[-1])

grid = [['.','.','.','.','.','.'],
		['.','0','0','.','.','.'],
		['0','0','0','0','.','.'],
		['0','0','0','0','0','.'],
		['.','0','0','0','0','0'],
		['0','0','0','0','0','.'],
		['0','0','0','0','.','.'],
		['.','0','0','.','.','.'],
		['.','.','.','.','.','.']]
length1 = len(grid)						#获取外层列表的长度
length2 = len(grid[length1-1])			#获取内层列表的长度
length = length1 - length2				#内外列表长度差


#把列表纵横交换打印出来，交换下标即可
#因列表长度不同，所以取列表长度差，再逐个打印
#若不取差值，就会报错：IndexError: list index out of range.
print(length)
for i in range(0,len(grid)-length):
	for j in range(0,len(grid[i])+length):
		print(grid[j][i],end = '')
	print('\n')
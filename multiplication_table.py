for i in range(1,10):
	for j in range(1,10):
		if i >= j:
			print( str(j) + 'x' + str(i) + '=' + str(int(i)*int(j)) + ' ',end = '')
		else:
			continue
	print('\n')
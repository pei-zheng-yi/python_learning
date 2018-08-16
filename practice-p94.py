def addToInventory(inventory,addedItems):
	count = {}
	for item in dragonLoot:
		count.setdefault(item,0)
		count[item] += 1
		# print(count)

# 此处注意：待新的计数字典完成后再进行下一步循环键是否在inv中
	for key in count.keys():
		if key in inv.keys():
			inv[key] = inv[key] + count[key]
		else:
			inv.setdefault(key,count[key])

def displayInventory(invs):
	print('Inventory:')
	item_total = 0
	for k,v in invs.items():
		print(str(v) + ' ' + k)
		item_total += v
	print('Total number of items: ' + str(item_total))

inv = {'gold coin':42,'rope':1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
count = addToInventory(inv,dragonLoot)
print(inv)
displayInventory(inv)
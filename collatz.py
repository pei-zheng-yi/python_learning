# def collatz(num):
# 	if num % 2 == 0:
# 		print(num//2)
# 	elif int(num) % 2 == 1:
# 		print(3 * num + 1)
# 	return



# num = int(input('请输入一个数值：'))
# while num != 1:
# 	collatz(num)


import sys
def collatz(number):
    print(number)
    if number == 1:
        sys.exit()
    elif number % 2 == 1 :
        number = number * 3 + 1
        collatz(number)
    else:
        number = number // 2
        collatz(number)
 
if __name__=='__main__':
    number = input('请输入一个整数: ')
    try:
        number = int(number)
        collatz(number)
    except ValueError as verror:
        print('ValueError: You need input digital.')
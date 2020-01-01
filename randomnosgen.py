# Program to generate n random unique secure keys of variable key length

from random import randint
alphanum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
			'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
			'1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

random_keys = []

n = int(input("Please enter the number of secure keys required: "))
for i in range(0,n):
	while True:
		sec_key = ''
		key_len = randint(5,10)
		for j in range(0,key_len):
			sec_key += alphanum[(randint(0,61))]
		if sec_key not in random_keys:
			random_keys.append(sec_key)
			break
		else:
			continue

print(random_keys)
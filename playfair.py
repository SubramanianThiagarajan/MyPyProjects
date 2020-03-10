def find_row_column(tem,a):
	for i in range(0,5):
		for j in range(0,5):
			if a[i][j] == tem:
				return i,j

#Main Program
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key='guidance'
len_key = len(key)
x=0
n=5
y=0
a = [[0] * n for i in range(n)]

for i in range(0,5):
	for j in range(0,5):
		if len_key>0:
			a[i][j] = key[x]
			x+=1
			len_key-=1
		else:
			while alp[y] == 'j' or (alp[y] in key):
				y+=1
				continue
			else:
				a[i][j] = alp[y]
				y+=1

for i in range(0,5):
	print('\n')
	for j in range(0,5):
		print(a[i][j],end=' ')

plain = 'balloon'
x=0
for i in range(0,len(plain)-1):
	if plain[i] == plain[i+1]:
		plain = plain[:i+1] + 'x' + plain[i+1:]

if len(plain) % 2 != 0:
	plain += 'z'

#Encryption
x=0
cipher = ''
for i in range(0,int(len(plain)/2)):
	temp = plain[x:x+2]
	r0,c0 = find_row_column(temp[0],a)
	r1,c1 = find_row_column(temp[1],a)

	if r0 == r1:
		cipher += a[r0][(c0+1)%5] + a[r0][(c1+1)%5]
	elif c0 == c1:
		cipher += a[(r0+1)%5][c0] + a[(r1+1)%5][c0]
	else:
		cipher += a[r0][c1] + a[r1][c0]
	x+=2
print("\n\nPlain Text is:" + plain)
print("\nCipher text is:"+ cipher)

#Decryption

x=0
plain1 = ''
plain2 = ''
for i in range(0,int(len(cipher)/2)):
	temp = cipher[x:x+2]
	r0,c0 = find_row_column(temp[0],a)
	r1,c1 = find_row_column(temp[1],a)
	if r0 == r1:
		plain1 += a[r0][(c0+4)%5] + a[r0][(c1+4)%5]
	elif c0 == c1:
		plain1 += a[(r0+4)%5][c0] + a[(r1+4)%5][c0]
	else:
		plain1 += a[r0][c1] + a[r1][c0]
	x+=2
for i in range(0,len(plain1)):
	if 'x' != plain1[i]:
		plain2 += plain1[i]
if plain2[-1] == 'z':
	plain2 = plain2[0:len(plain2)-1]
print("\n\nPlain Text is:" + plain2)
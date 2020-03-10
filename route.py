import random as ran
import math
import sys

def find_row_column(tem,a):
	for i in range(0,5):
		for j in range(0,5):
			if a[i][j] == tem:
				return i,j


def route_encrypt(m,n,plain_text):
	
	x = 0;y=0;
	matrix = []
	encrypted_text = ""

	for i in range(n):
		matrix_row = []
		for j in range(m):
			if i*m+j < len(plain_text):
				matrix_row.append(plain_text[i*m+j])
			else:
				matrix_row.append("z")
		matrix.append(matrix_row)

	for i in range(n):
		print(matrix[i])

	while(x<m and y<n):

		
		for i in range(y, m):
			encrypted_text += matrix[x][i]
		x+=1
		        		
		for i in range(x, n):
			encrypted_text += matrix[i][m-1]			
		m-=1
        		
		if (x < n):
			for i in range(m-1, y-1, -1):
				encrypted_text += matrix[n-1][i]
			n-=1

		if(y < m):
			for i in range(n-1, (x-1),-1):
				encrypted_text += matrix[i][y]
			y+=1	

	return encrypted_text                               


def route_decrypt(m,n,cipher):
    
    x = 0;y=0;z=0;
    n1=n;m1=m;
    matrix = []
    decrypted_text = ""
    decrypt_text = ""
    for i in range(n):
        matrix_row = []
        for j in range(m):
                matrix_row.append('z')
        matrix.append(matrix_row)
    
         
    while(x<m and y<n):

        
        for i in range(y, m):
            matrix[x][i]=cipher[z]
            z+=1;
        x+=1;
                        
        for i in range(x, n):
            matrix[i][m-1]=cipher[z]
            z+=1;
        m-=1;
                
        if (x < n):
            for i in range(m-1, y-1, -1):
                matrix[n-1][i]=cipher[z]
                z+=1;
            n-=1;

        if(y < m):
            for i in range(n-1, (x-1),-1):
                matrix[i][y]=cipher[z]
                z+=1;
            y+=1;

    for i in range(n1):
                print(matrix[i])

    for i in range(n1):
        for j in range(m1):
            decrypted_text+=matrix[i][j]
    decrypted_text=list(decrypted_text)
    while(decrypted_text[-1]=='z'):
    	decrypted_text.pop()
    for i in decrypted_text:
    	decrypt_text+=i

    return decrypt_text

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

plain = 'startthewar'
plain = plain.lower()
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
print("\nCipher text is (Playfair Cipher):"+ cipher)

#Route Cipher
q = len(cipher)

while(1):
	if q%6 == 0:
		break
	else:
		q+=1

d1 = dict()

for i in range(3,q//2):
	if (q%i == 0) and (q//i > 2):
		d1.update({i:q//i})

d2 = list(d1)

r1 = d2[ran.randint(0,len(d2)-1)]

for ke,va in d1.items():
	if(ke==r1):
		rows = ke
		cols = va

cipher1 = route_encrypt(cols,rows,cipher)

print("\nThe Cipher Text after route cipher is:",cipher1)

print("\nTransmitting data.................")
print("\nRecieved Data:",cipher1,rows,"x",cols)


plain_text1 = route_decrypt(cols,rows,list(cipher1))
print("\nDecrypted text after Route Cipher:",plain_text1)
#Decryption

x=0
plain1 = ''
plain2 = ''
for i in range(0,int(len(plain_text1)/2)):
	temp = plain_text1[x:x+2]
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
print("\n\nPlain Text is(After Decryption Playfair):" + plain2)

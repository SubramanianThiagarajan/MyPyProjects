#Hamming code generator

#Initialising the arrays
P1 = [2,4,6,8,10,12,14]
P2 = [2,5,6,9,10,13,14]
P3 = [4,5,6,11,12,13,14]
P4 = [8,9,10,11,12,13,14]

#Function to get the data
def get_data(n):
	
	data = str(input("Enter the data only in 1s and 0s: "))
	while n != len(data):
		print("Please enter correct data");
		data = input("Enter the data only in 1s and 0s: ")
	return data

#Function to predict the number of parity bits
def no_of_parity(n):
	if n<=4:
		p = 3
	elif n>4 and n<=12:
		p = 4
	return p

#Return 1 or 0
def get_0_1(e):
	if(e == 1):
		return '0'
	else:
		return '1'
def get_1_0(e):
	if(e==1):
		return '1'
	else:
		return '0'
#Get the appropriate array
def get_P(j):
	switcher = {
		0 : P1, 1 : P2, 2 : P3 , 3 : P4}
	return switcher.get(j,[])

#Parity update function
def parity_updater(P,l,res,k,o_e):
	x = 0
	for j in range(0,l):
		if j in P:
			x += int(res[j])

	if x%2 == 0:
		res.pop(k)
		res.insert(k,get_0_1(o_e))
	else:
		res.pop(k)
		res.insert(k,get_1_0(o_e))
	return res

#Main program
ch = 1
while(ch):
	res = []
	A = [0 , 1 , 3 , 7]
	#data size
	n = int(input("How many digits you want to transmit (>1): "))

	#data
	data = get_data(n)

	#Number of parity bits
	p = no_of_parity(n)
	i = 0
	z = n - 1
	oddoreven = 1

	#Get from user whether even parity or odd parity
	print("\nParity type\n1.Even parity\n2.Odd parity\n")
	oddoreven = int(input("Which parity do you want(1 or 2):"))

	#Creating an array for result
	for i in range(0,p+n):
		if (i in A):
			res.insert(i,'-')
		else:
			res.insert(i,data[z])
			z = z - 1

	#Parity update call
	for j in range(0,p):
		res = parity_updater(get_P(j),p+n,res,(pow(2,j) - 1),oddoreven)

	#Display the hamming code
	s = ""
	for i in range(p+n-1,-1,-1):
		s += str(res[i]) + " "
	print("\n\nResult is: " + s +"\n")

	#Do you want to continue
	ch = int(input("Do you want to continue YES - 1 : NO - 0:"))
	if(ch == 0):
		print("\nThank you for using the hamming code generator\n")

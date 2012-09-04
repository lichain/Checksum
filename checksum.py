def mychecksum(x):
	print x
	s_index = 0
	e_index = len(x)
	delta = 2

	hex_sum = 0
	ten_sum = 0
	y = ""

	for i in range(s_index, e_index, delta):
		y = x[s_index : s_index+delta]
		s_index = s_index +delta
		
		if (y.strip() == ""):
			break
		ten_sum = ten_sum + int(str(y),16)
		#print "hex: " + y + " -->(ten): " + str(int(y,16))

	hex_sum = hex(ten_sum)
	print "sum of ten: " + str(ten_sum) + " --> sum of hex: " + str(hex_sum)

	len_hex_sum = len(str(hex_sum))
	hex_check_bit = str(hex_sum)[len_hex_sum-2:len_hex_sum]

	result = ("00" == hex_check_bit)
	
	print "Checksum string: " + x + " is " + str(result)

#x = "10000000020003787FE4F6D8FD75812B02004A02D6" 
#mychecksum(x)

f = open('data.txt')
while True:
	line = f.readline()
	#print line
	if(len(line) == 0):
		break
	mychecksum(str(line))
f.close()
	

import binascii

def xor(s1, s2):
	resultarray = []
	for byte1, byte2 in zip(s1, s2):
		resultarray.append(byte1 ^ byte2)
	result = bytes(resultarray)
	return result
	

import binascii

def b64ToHex(b64String):
	binarystr = binascii.a2b_base64(b64String) # converts b64 to binary
	hexstr = binascii.hexlify(binarystr) # converts binary to hex
	return hexstr
	
def hexToB64(hexString):
	binarystr = binascii.unhexlify(hexString) # converts hex to binary
	b64str = binascii.b2a_base64(binarystr, newline = False) # converts binary to b64
	return b64str
import collections
from s1c02 import xor
import binascii

'''
From this point on, I'm not providing the number of arguments.
Part of your job is to understand the contracts of these methods
and how they fit together.
'''

def caesarEncrypt(key, plaintext):
	resultarray = []
	for i in range(len(plaintext)):
		resultarray.append(key)
	result = b"".join(resultarray)
	return xor(plaintext, result)

def caesarDecrypt(key, ciphertext):
	resultarray = []
	for i in range(len(ciphertext)):
		resultarray.append(key)
	result = b"".join(resultarray)
	return xor(ciphertext, result)

def scoreText(bytestring):
	print(bytestring)
	freqTable = collections.Counter(bytestring)
	print(freqTable)
	#for key in freqTable.keys():
	#	freqTable[key] = freqTable[key]/len(bytestring)
	return freqTable
	
	
def solveS1C03(ciphertext):
	pass

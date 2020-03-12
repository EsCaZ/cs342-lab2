import collections
from s1c02 import xor

'''
From this point on, I'm not providing the number of arguments.
Part of your job is to understand the contracts of these methods
and how they fit together.
'''

def caesarEncrypt(key, plaintext):
	resultarray = []
	for i in range(len(plaintext)):
		resultarray.append(key)
	return xor(plaintext, bytes(resultarray))

def caesarDecrypt(key, ciphertext):
	return xor(ciphertext, key)

def scoreText(bytestring):
	freqTable = collections.Counter(bytestring)
	#for key in freqTable.keys():
	#	freqTable[key] = freqTable[key]/len(bytestring)
	return freqTable
	
	
def solveS1C03(ciphertext):
	pass

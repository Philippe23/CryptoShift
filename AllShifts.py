#!/usr/bin/env python

import argparse

kLOWERCASE_MIN = ord('a')
kLOWERCASE_MAX = ord('z')
kUPPERCASE_MIN = ord('A')
kUPPERCASE_MAX = ord('Z')

def parseArgs():
	parser = argparse.ArgumentParser(description='Applies all 25 Caesar shifts to input')
	parser.add_argument('input', metavar='TEXT', nargs='+', 
	                    help='The text to apply the cipher to')
	opts = parser.parse_args()
	
	opts.input = ' '.join(opts.input)
	
	return opts

def casearCipherShiftChar(c, shift):
	t = ord(c)
	if t >= kLOWERCASE_MIN and t <= kLOWERCASE_MAX:
		bnds = (kLOWERCASE_MIN, kLOWERCASE_MAX)
	elif t >= kUPPERCASE_MIN and t <= kUPPERCASE_MAX:
		bnds = (kUPPERCASE_MIN, kUPPERCASE_MAX)
	else:
		return c
	
	t += shift
	t -= bnds[0]
	t %= 26
	t += bnds[0]
	assert(t >= bnds[0])
	assert(t <= bnds[1])
	
	return chr(t)	
		

def caesarCipher(input, shift):
	res = ''
	for c in input:
		res += casearCipherShiftChar(c, shift)
	return res


if __name__ == "__main__":
	opts = parseArgs()
	print('input     : ' + opts.input)
	for s in range(1, 26):
		print('output[{0:#02}]: {1}'.format(s, caesarCipher(opts.input, -s)))
	
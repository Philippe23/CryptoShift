#!/usr/bin/env python

import argparse

kLOWERCASE_MIN = ord('a')
kLOWERCASE_MAX = ord('z')
kUPPERCASE_MIN = ord('A')
kUPPERCASE_MAX = ord('Z')

def parseArgs():
	parser = argparse.ArgumentParser(description='Applies Caesar shift to input')
	parser.add_argument('--shift', '-s', dest='shift', action='store',
	                    type=int, default=1, help='num chars to shift, 1: B->A, -2: A->C')
	parser.add_argument('input', metavar='TEXT', nargs='+', 
	                    help='The text to apply the cipher to')
	opts = parser.parse_args()
	
	opts.shift = -opts.shift % 26
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
		

def caesarCipher(opts):
	res = ''
	for c in opts.input:
		res += casearCipherShiftChar(c, opts.shift)
	opts.output = res

def printResults(opts):
	print('input:  ' + opts.input)
	print('output: ' + opts.output)

if __name__ == "__main__":
	opts = parseArgs()
	caesarCipher(opts)
	printResults(opts)
	
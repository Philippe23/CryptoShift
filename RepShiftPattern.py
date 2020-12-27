#!/usr/bin/env python

import argparse
import sys

kLOWERCASE_MIN = ord('a')
kLOWERCASE_MAX = ord('z')
kUPPERCASE_MIN = ord('A')
kUPPERCASE_MAX = ord('Z')
kDIGIT_MIN = ord('0')
kDIGIT_MAX = ord('9')

def parseArgs():
	parser = argparse.ArgumentParser(description='Applies a repeating Caesar shift to input')
	parser.add_argument('--pattern', '-p', dest='pattern', action='store',
	                    default='1', help='num chars to shift, 15: AA -> BF')
	parser.add_argument('input', metavar='TEXT', nargs='+', 
	                    help='The text to apply the cipher to')
	opts = parser.parse_args()
	
	pattern = []
	for c in opts.pattern:
		c_ord = ord(c)
		bnds = None
		if c_ord >= kLOWERCASE_MIN and c_ord <= kLOWERCASE_MAX:
			bnds = (kLOWERCASE_MIN, kLOWERCASE_MAX)
		elif c_ord >= kUPPERCASE_MIN and c_ord <= kUPPERCASE_MAX:
			bnds = (kUPPERCASE_MIN, kUPPERCASE_MAX)
		elif c.isdigit():
			bnds = (kDIGIT_MIN, kDIGIT_MAX)
		else:
			print('ERROR: Unable to convert "{0}" to pattern entry'.format(c))
			sys.exit(1)
		pattern.append(bnds[0] - c_ord)

	if len(pattern) < 1:
		print('ERROR: invalid empty pattern', file=sys.stderr)
		sys.exit(1)
	opts.string_pattern = opts.pattern
	opts.pattern = pattern
	
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
		

def patternShift(input, pattern):
	res = ''
	i = 0
	PATTERN_LEN = len(pattern)
	for c in input:
		c_ord = ord(c)
		if ((c_ord >= kLOWERCASE_MIN and c_ord <= kLOWERCASE_MAX) or 
		   (c_ord >= kUPPERCASE_MIN and c_ord <= kUPPERCASE_MAX)):
			res += casearCipherShiftChar(c, pattern[i % PATTERN_LEN])
			i += 1
		else:
			res += c
		
	return res


if __name__ == "__main__":
	opts = parseArgs()
	print('shift pattern: ' + opts.string_pattern)
	print('input:  ' + opts.input)
	print('output: ' + patternShift(opts.input, opts.pattern))
	
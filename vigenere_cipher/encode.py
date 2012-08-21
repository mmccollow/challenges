#!/usr/bin/env python

KEY = 'GLADOS'
KEYLEN = len(KEY)

def encode(text):
	pad = _pad_key(len(text))
	return ''.join(map(_letter_cipher, tuple(pad), tuple(text)))

def _letter_cipher(pad_letter, src_letter):
	# this works for ASCII only
	offset = 65
	summed = (ord(pad_letter) - offset) + (ord(src_letter) - offset)
	if summed > 25: # go past Z, wrap around to A and continue
		summed -= 26
	return chr(summed + offset)

def _pad_key(length):
	# I wish I knew how to make this whole function more Pythonic
	# (contact me with any tips!)
	key = tuple(KEY)
	pad = ''
	counter = 0
	while counter < length:
		for i in range(0, KEYLEN):
			if counter >= length:
				break
			counter += 1
			pad += key[i]
	return pad


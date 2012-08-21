#!/usr/bin/env python

KEY = 'GLADOS'

def encode(text, op='encode'):
	pad = _pad_key(len(text))
	if op == 'encode':
		return ''.join(map(_letter_cipher, tuple(pad), tuple(text)))
	if op == 'decode':
		return ''.join(map(_letter_decipher, tuple(pad), tuple(text)))

def decode(text):
	return encode(text, 'decode')

def _letter_cipher(pad_letter, src_letter):
	# this works for ASCII only
	offset = 65 # 65 = ASCII capital A
	summed = (ord(pad_letter) - offset) + (ord(src_letter) - offset)
	if summed > 25: # go past Z, wrap around to A and continue
		summed -= 26
	return chr(summed + offset)

def _letter_decipher(pad_letter, src_letter):
	offset = 65
	dist = (ord(src_letter) - offset) - (ord(pad_letter) - offset)
	if dist < 0:
		dist = 25 + (dist + 1)
	return chr(dist + offset)

def _pad_key(length):
	# I wish I knew how to make this whole function more Pythonic
	# (contact me with any tips!)
	key = tuple(KEY)
	pad = ''
	counter = 0
	while counter < length:
		for i in range(0, len(KEY)):
			if counter >= length:
				break
			counter += 1
			pad += key[i]
	return pad


#!/usr/bin/env python

def intersect(a, b):
	t = set.intersection(
		set([(x,y) for x in range(a[0], a[2]+1) for y in range(a[1], a[3]+1)]),
		set([(x,y) for x in range(b[0], b[2]+1) for y in range(b[1], b[3]+1)])
	)
	if len(t) == 0:
		return None
	return [
		min([x[0] for x in t]),
		min([y[1] for y in t]),
		max([x[0] for x in t]),
		max([y[1] for y in t])
	]

# Test cases (should both return True):
# intersect([3,3,10,10], [6,6,12,12]) == [6, 6, 10, 10]
# intersect([4,4,5,5], [6,6,10,10]) == None

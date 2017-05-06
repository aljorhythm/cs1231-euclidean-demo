# -*- coding: utf-8 -*-
# implementation of euclidean algorhythm

import sys
import pprint
import math

pp = pprint.PrettyPrinter(indent=4, width=1)

# do k number of times
def mod_exponentiate(n, k, modulo):
	res = {
		'n' : n,
		'results' : []
	}
	power = 1
	mod = n
	for x in range(k - 1):
		resN = {
			'power' : power,
			'mod' : mod
		}
		power = power * 2
		res['results'].append(resN)
		mod = math.pow(mod, 2) % modulo
	return res

n = 216
k = 8
modulo = 1537

print "n = {0}, k = {1}, modulo = {2}\n".format(n, k, modulo)

mod_res = mod_exponentiate(216, 8, 1537)

n = mod_res['n']

refactored_results = {}

for resN in mod_res['results']:
	refactored_results[resN['power']] = resN['mod']
	print str(n) + ' ^ ' + str(resN['power']) + ' ' +  u'≡' + ' ' + str(resN['mod'])
print ''

selected_indices = [1, 2, 4, 8, 32]
index =  reduce(lambda x, y: x+y, selected_indices)

print 'selected indices: '
pp.pprint(selected_indices)
print 'sum of indices = {0}'.format(index)
print ''

print 'results: '
pp.pprint(refactored_results)
print ''

selected_Rs = { refactored_results[key] for key in refactored_results if key in selected_indices}
multiplied_together = reduce(lambda x, y: x*y, selected_Rs)
print 'multipled ' + str(multiplied_together)
print '{0} ^ {1} mod {2} = '.format(n, index, modulo) + str( multiplied_together % 1537 )

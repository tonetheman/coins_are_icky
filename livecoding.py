

import random

def toss_coin():
	return random.sample(["heads","tails"],1)[0]

def test_toss_coin():
	results = { "heads" : 0, "tails" : 0 }

	for i in range(100):
		tmp = toss_coin()
		results[tmp] = results[tmp] + 1


	return results

def flipper(target):
	results = [ toss_coin(), toss_coin() ]

	while target != results[-2:]:
		results.append(toss_coin())
		# results.append(toss_coin())


	return results


def test_flipper(target):
	results = []
	for i in range(10000):
		results.append(len(flipper(target)))

	return results

import numpy

print "heads,heads",numpy.mean(test_flipper(["heads","heads"]))
print "heads,tails", numpy.mean(test_flipper(["heads","tails"]))



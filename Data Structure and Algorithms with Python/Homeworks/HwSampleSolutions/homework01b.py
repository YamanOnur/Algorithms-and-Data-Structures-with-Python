"""
METU CENG310 Spring 2020-2021
Homework-01B Solutions
@author: Mehmet Taha Şahin
"""

#R-1.9
range(50,81,10)

#R-1.11
[2**x for x in range(0,9)]

#C-1.19
[chr(x) for x in range(97,123)]

#C-1.28
def norm(v,p=2):
	return sum([x**p for x in v])**(1/p)

#P-1.35
from random import randint
tests=100 #test number can be changed for more accuracy
for n in range(5,101,5):
	found = 0
	for t in range(tests):
		bd_set = []	
		for p in range(0,n):
			bd_set.append(randint(1,365))
			if bd_set[-1] in bd_set[0:-1]:
				found = found + 1
				break	
	print("BDayParadox(" + str(n) + "): " + str(found) + " times birthday pairs found for " + str(tests) + " test.")
	print("ratio: " + str(found/tests))
		
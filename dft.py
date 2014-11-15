from numpy import *
from math import *
import cmath

N = int(raw_input('enter upto which point you want to find out the dft that is N: '))

data = []
n = int(raw_input('enter how many elements you want in the sequence of the input:'))
for i in range(0, n):
	x = int(raw_input('enter the numbers into the array: '))
	data.append(x)

if N < n:

	print "invalid inputs"
	
elif N == n:
	print "your data for the dft is : "
	print(data)
else:

	p = N - n 
	for i in range(0, p):
		data.append(0)
	print "your data for the dft is : "
	print(data)

i = (-2 * cmath.pi) / N

w = cmath.e ** (0 +  i * 1j)
#p = e ** (0 + 1j)
#print p

angle = angle(w, deg = True)
print "angle of the matrix element w is: "
print angle, "degree"

a = array([])
for i in range(0, N):
	a = append(a, 1)

row_array = []
for k in range(1, N):
	for l in range(0, k * N, k):
		row_array.append(w ** l)
	a = vstack([a, row_array])
	row_array = []
print "the w matrix is : "
print a
print "DFT is : "
b =  a * data
b =  b.sum(axis = 1)

dft = []
print "["
for i in range(0, N):
	print "[", b[i], "]"
print "]"
print "have a nice day :) :) and don't forget to try again :) "
	




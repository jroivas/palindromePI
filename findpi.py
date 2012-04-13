#!/usr/bin/python
import math

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

def isPalindrome(s):
	c=len(s)
	if c<=1: return False
	if c==2:
		if s[0] == s[1]: return True
		else: return False

	m = int(c/2)
	for n in range(0,m):
		if s[n] != s[c-n-1]: return False

	return True

def filterPalindrome(n,minlen):
	res = []
	for i in n:
		s="%d"%i
		c=len(s)
		if (c>=minlen):
			if isPalindrome(s):
				res = res+[i]
	return res

def readPi():
	# Assume we have precalc'd pi
	# This one is from: http://www.archive.org/stream/Pi_to_100000000_places/pi.txt
	pi = ""
	p = open("pi.txt")
	line = p.readline()
	while 1:
		if not line: break
		pi += line.strip().replace(' ','')
		line = p.readline()
		
	p.close()
	return pi

# Read PI value
mypi = readPi()

# Filter primes under 9999999, min length 7
primes = filterPalindrome(primes(9999999),7)

best = 99999999
val = -1
for i in primes:
	pos = mypi.find("%d"%i)
	if pos>0 and best>pos:
		best = pos
		val = i

print val

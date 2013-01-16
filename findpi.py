#!/usr/bin/python
import math

def primes(n, minimum): 
    """ Calculate primes up to given number
    Filter out smaller than minimum primes

    >>> primes(2, 0)
    [2]
    >>> primes(10, 0)
    [2, 3, 5, 7]
    >>> primes(100, 50)
    [53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    if n == 2:
        return [2]
    elif n < 2:
        return []

    s = list(range(3, n + 1, 2))
    mroot = n ** 0.5
    half = (n + 1)/2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = int((m * m - 3) / 2)
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3

    if minimum <= 2:
       res = [2] 
    else:
        res = []
    res += [x for x in s if x and x >= minimum]
    return res

def isPalindrome(i):
    """ Check if number is palindrome

    >>> isPalindrome(99)
    True
    >>> isPalindrome(999)
    True
    >>> isPalindrome(9990)
    False
    >>> isPalindrome(1991)
    True
    >>> isPalindrome(9999)
    True
    >>> isPalindrome(99199)
    True
    >>> isPalindrome(4242)
    False
    >>> isPalindrome(4224)
    True
    >>> isPalindrome(123454321)
    True
    >>> isPalindrome(123454311)
    False
    """

    if i < 10:
        return False
    if i < 100:
        a = int(i / 10)
        b = i % 10
        if a == b:
            return True
        return False

    s = str(i)
    c = len(s)
    m = int(c / 2)
    a = s[:m]
    if m * 2 == c:
        b = s[m:]
    else:
        b = s[m + 1:]
    b = b[::-1]

    return a == b

def filterPalindrome(n, minlen):
    for i in n:
        if i >= minlen and isPalindrome(i):
            yield i

def searchPalindromeFromPi(primes):
    best = maxnum
    val = -1

    strs = [str(i) for i in primes]

    with open('pi.txt', 'r') as p:
        prev = ''
        while True:
            line = p.readline()
            if not line:
                break
            line = line.strip().replace(' ', '')
            haystack = prev + line
            candidates = []
            for i in strs:
                pos = haystack.find(i)
                if pos > 0:
                    candidates.append((pos, i))
            if candidates:
                res = sorted(candidates)
                val = res[0][1]
                return val
            prev = line

    return val

if __name__ == '__main__':
    # Filter primes under 9999999, min length 7
    numlen = 7
    minnum = int('1' + '0' * (numlen - 1))
    maxnum = int('9' * numlen)
    primes = filterPalindrome(primes(maxnum, minnum), minnum)

    # Search proper palindrome prime from Pi
    val = searchPalindromeFromPi(primes)

    print (val)

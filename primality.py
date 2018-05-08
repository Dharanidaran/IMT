# primality.py


import math
import time

knowPrimes = [2,3]


def printPrime( primeRange = 100):

	startTime = time.time()
	for number in range(5,primeRange,2):
	    isprime = True
	    for smallprime in knowPrimes:
	        if number % smallprime == 0:
	            isprime = False
	            # print(" I am not prime number",number)
	            break
	        else:
	            if smallprime > math.sqrt(primeRange):
	                break
	            else:
	                pass


	            # pass

	    if isprime == True:
	        knowPrimes.append(number)

	print(len(knowPrimes))
	print("Time taken in seconds " ,time.time()-startTime)


printPrime(100000)
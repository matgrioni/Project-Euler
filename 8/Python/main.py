#!/usr/bin/python

import time
import operator

# Converts each element in l to an int and returns the resulting list.
def listToInt(l):
    return [int(x) for x in l]

internal = ("73167176531330624919225119674426574742355349194934"
            "96983520312774506326239578318016984801869478851843"
            "85861560789112949495459501737958331952853208805511"
            "12540698747158523863050715693290963295227443043557"
            "66896648950445244523161731856403098711121722383113"
            "62229893423380308135336276614282806444486645238749"
            "30358907296290491560440772390713810515859307960866"
            "70172427121883998797908792274921901699720888093776"
            "65727333001053367881220235421809751254540594752243"
            "52584907711670556013604839586446706324415722155397"
            "53697817977846174064955149290862569321978468622482"
            "83972241375657056057490261407972968652414535100474"
            "82166370484403199890008895243450658541227588666881"
            "16427171479924442928230863465674813919123162824586"
            "17866458359124566529476545682848912883142607690042"
            "24219022671055626321111109370544217506941658960408"
            "07198403850962455444362981230987879927244284909188"
            "84580156166097919133875499200524063689912560717606"
            "05886116467109405077541002256983155200055935729725"
            "71636269561882670428252483600823257530420752963450")

print("An internal 1000 digit number is assumed. This program finds the n")
print("adjacent digits in the number with the largest product")
n = int(raw_input("Enter n > "))

start = time.time()

# Values to start off the loop iteration.
first = internal[0]
m = reduce(operator.mul, listToInt(internal[:n]), 1)

# Loop goes through the entire string gettting consecutive substrings of
# length n.
for i in range(1, len(internal)-n+1):
    # If the last digit of the new substring is greater than the first
    # digit of the prior substring, this has a chance of being a new largest
    # solution.
    #
    # eg. (1234)5345 --> 1(2345)345, 234 are in both strings but the first and
    # last are what matter.
    last = internal[i+n-1]
    if last > first:
        # Foldl the substring to get the product
        prod = reduce(operator.mul, listToInt(internal[i:i+n]), 1)
        
        if prod > m:
            m = prod

    first = internal[i]

end = time.time()

print("Result: {}".format(m))
print("{} s".format(end - start))

#!/usr/bin/python

import time

def triplet(n):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a + b > n:
                break

            for c in range(1, n+1):
                if a + b + c == n and a*a + b*b == c*c:
                    return (a, b, c)

                if a + b+ c > n:
                    break
                    

print("Returns a pythagorean triplet where a + b + c = n, and calculates abc")
n = int(raw_input("Enter n > "))

start = time.time()
answer = triplet(n)
end = time.time()

print("Result: {}".format(answer))
print("abc = {}".format(answer[0] * answer[1] * answer[2]))
print("{} s".format(end - start))

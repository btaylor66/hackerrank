#!/usr/bin/env python
import math
import os
import random
import re
import sys


def sockMerchant(n,ar):
    #result = sockMerchant(n, ar)
    #result = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    ar_set = list(set(ar))
    pairs = 0
    for x in range(0,len(ar_set)):
        print(ar_set[x],ar.count(ar_set[x]), int(ar.count(ar_set[x])/2))
        pairs += int(ar.count(ar_set[x])/2)
    return pairs

def countingValleys(n, s):
    #result = countingValleys(n, s)
    #result = countingValleys(8, 'UDDDUDUU')
    #print(result)
    alt = 0
    valleys = 0
    mountains = 0
    for x in range(0,len(s)):
        if s[x] == 'U':
            alt += 1
            if alt == 0:
                #print('valley')
                valleys += 1
        else:
            alt -= 1
            if alt == 0:
                #print('mountain')
                mountains += 1
        #print(s[x],alt)
    return valleys

def jumpingOnClouds(c):
    #result = jumpingOnClouds([0,0,1,0,0,1,0])
    #print(result)
    jumps = 0
    x = 0
    while x < len(c)-1:
        if  x<len(c)-2 and (c[x+2] == 0):
            jumps += 1
            x += 2
        else:
            jumps +=1
            x += 1
        print(x,jumps)
    return jumps

def twoDarray(arr):
    #result = twoDarray([[-9, -9, -9, 1, 1, 1],
    #                    [0, -9, 0, 4, 3, 2],
    #                    [-9, -9, -9, 1, 2, 3],
    #                    [0, 0, 8, 6, 6, 0],
    #                    [0, 0, 0, -2, 0, 0],
    #                    [0, 0, 1, 2, 4, 0]])
    #print(result)
    rows = len(arr)
    max = -99999
    for x in range(rows-2):
        for y in range(rows-2):
            print(arr[x][y],arr[x][y+1],arr[x][y+2])
            print(' ',arr[x+1][y+1])
            print(arr[x+2][y],arr[x+2][y+1],arr[x+2][y+2])
            sum = arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x+1][y+1]+arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2]
            if sum > max:
                max = sum
    return max

def rotLeft(a, d):
    #result = rotLeft(4, [1,2,3,4,5])
    start = d[:a]
    end = d[a:]
    d = end + start
    return d

def minimumBribes(q):
    trades = 0
    for x in range(len(q)):

        if abs(q[x] - (x+1)) <= 2:

            if ( x < len(q)-1) and (q[x] > q[x+1]):
                print(x, q[x],abs(q[x] - (x+1)))
                trades += abs(q[x] - (x+1))
        elif x < (len(q)-1) and abs(q[x] - (x+1)) > 2:
            print(x, q[x],x+1,'Too chaotic')
            return
    print(trades)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #n = int(input())
    #ar = list(map(int, input().rstrip().split()))
    result = minimumBribes([2,1,5,3,4])
    result = minimumBribes([1,2,5,3,7,8,6,4])

    #fptr.write(str(result) + '\n')
    #fptr.close()
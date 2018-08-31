#!/usr/bin/python3


def tuples():
    n = int(input())
    integer_list = map(int, input().split())

    print(hash(tuple(integer_list)))

def wrap(string, max_width):
    from textwrap import TextWrapper
    wrapper = TextWrapper(width=max_width)
    return wrapper.fill(text=string)

def text_wrap():

    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

def door_mat():
    import math
    rows, cols = input().split()
    rows = int(rows)
    cols = int(cols)
    for i in range(1,rows+1):
        if i == math.ceil(rows/2):
            dashes = int((cols-7)/2)
            print(dashes*"-"+"WELCOME"+dashes*"-")
        elif i > rows/2:
            dashes = int((cols-((rows+1-i)*2-1)*3)/2)
            print(dashes*"-"+((rows+1-i)*2-1)*".|."+dashes*"-")
        else:
            dashes = int((cols-(i*2-1)*3)/2)
            print(dashes*"-"+(i*2-1)*".|."+dashes*"-")

def string_format():
    dec = int(input())
    w = len(bin(dec))-1
    for i in range (1,dec+1):
        print('{0:>{width}d}{0:>{width}o}{0:>{width}X}{0:>{width}b}'.format(i, width=w))

def alpha_rangoli():
    import string
    n = int(input())
    alphabet = list(string.ascii_lowercase)

    for i in range(0,n):
        dashes = (n-1-i)*2
        row = ""
        for j in range(n-i,n+1):
            if j == (n-i):
                row += alphabet[n-i-1]
            else:
                row = alphabet[j-1]+"-"+row+"-"+alphabet[j-1]
        row = dashes*"-"+row+dashes*"-"
        print(row)
    for i in range(n-2,-1,-1):
        dashes = (n-1-i)*2
        row = ""
        for j in range(n-i,n+1):
            if j == (n-i):
                row += alphabet[n-i-1]
            else:
                row = alphabet[j-1]+"-"+row+"-"+alphabet[j-1]
        row = dashes*"-"+row+dashes*"-"
        print(row)

def capitalize():
    s = input()
    name = ""
    last = " "
    for i in s:
        if last == ' ':
            name = name + i.capitalize()
        else:
            name = name + i
        last = i

    print(name)

def string_validator(s):
    #s = input()
    resp = False
    for c in s:
        if c.isalnum():
            resp = True
            break
    print(resp)
    resp=False
    for c in s:
        if c.isalpha():
            resp = True
            break
    print(resp)
    resp=False
    for c in s:
        if c.isdigit():
            resp = True
            break
    print(resp)
    resp=False
    for c in s:
        if c.islower():
            resp = True
            break
    print(resp)
    resp=False
    for c in s:
        if c.isupper():
            resp = True
            break
    print(resp)


if __name__ == '__main__':
    string_validator('qA2')

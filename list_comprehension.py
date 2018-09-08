#!/usr/local/bin/python3


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

def swap_case(s):

    phrase = ""
    for c in s:
        if c.islower():
            phrase += c.upper()
        elif c.isupper():
            phrase += c.lower()
        else:
            phrase += c

    print(phrase)

def minion_game(s):
    #Stuart
    print(len(s))
    x = 0
    stuart = 0
    for c in s.upper():
        word =""
        if c not in 'AEIOU':
            stuart += len(s)-x

        x += 1
    x = 0
    kevin = 0
    for c in s.upper():
        word =""
        if c in 'AEIOU':
            kevin += len(s)-x

        x += 1
    if kevin > stuart:
        print('Kevin %i', kevin)
    elif stuart > kevin:
        print('Stuart %i', stuart)
    else:
        print("Draw")

def compress_string(s):
    last = None
    compressed = []
    x = 1
    for c in s:
        if int(c) == last:
            x += 1
        else:
            if last != None:
                compressed.append((x,last))
            last = int(c)
            x = 1
    compressed.append((x,last))
    for i in compressed:
        #print(i, end=" ")
        print(i)

def iterables_iterator(n,s,k):
    s = s.split()
    # They are assuming index of 1 not 0
    k = k - 1
    # Character to search for
    c = s[k]
    output = []
    count = 0

    for a in range(n):
        for b in range(a+1,n):
            output.append((s[a],s[b]))
    print(output)
    for t in output:
        if c in t:
            #print(t)
            count += 1
    print(count,len(output))
    print(count/float(len(output)))

if __name__ == '__main__':
    iterables_iterator(4,"a a c d",2) # =.83333
    iterables_iterator(9,"a b c a d b z e o",4) # =.72222
    iterables_iterator(9,"a a a a d e u o i",3) # =.88095


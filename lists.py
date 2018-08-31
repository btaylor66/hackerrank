#!/usr/bin/python3

if __name__ == '__main__':
    myList = []

    n = int(input())

    for i in range(0,n):
        command = input().split(' ')
        if command[0] == 'append':
            myList.append(int(command[1]))
        elif command[0] == 'remove':
            myList.remove(int(command[1]))
        elif command[0] == 'insert':
                myList.insert(int(command[1]),int(command[2]))
        elif command[0] == 'sort':
            myList.sort()
        elif command[0] == 'reverse':
            myList.reverse()
        elif command[0] == 'pop':
            myList = myList[:-1]
        elif command[0] == 'print':
            print(myList)
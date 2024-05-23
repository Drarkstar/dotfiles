import sys

def ricerca_binaria():
    l = 0
    r = 100
    # print(input(), input())
    inp = ""
    while inp != "!":
        m = int(round((r+l)/2))
        print(m)
        print(m, file=sys.stderr)
        inp = input()
        if inp == "<":
            # print("il numero è più piccolo")
            r = m-1
        elif inp == ">":
            # print("il numero è più grande")
            l = m+1

ricerca_binaria()
#pytest.py
import sys
import random
print("a che numero sto pensando", file=sys.stderr)
rand = random.randrange(0, 100)
print(rand, file=sys.stderr)
inp = int(input())
count = 0
while rand != inp:
    if inp > rand:
        print("il numero è più piccolo", file=sys.stderr)
        print("<")
    elif inp < rand:
        print("il numero è più grande", file=sys.stderr)
        print(">")
    count +=1
    inp = int(input())
print("!")
print("{} tentativi".format(count), file=sys.stderr)

# print ("Hello World", file=sys.stderr) # print on error channel
# print(s)



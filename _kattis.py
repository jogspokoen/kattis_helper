import sys

n = int(sys.stdin.readline()[:-1])
s = sys.stdin.readline()[:-1]
ss = [s[:-1] for s in sys.stdin.readlines()]
nn = [int(n[:-1]) for n in sys.stdin.readlines()]

n, m = map(int, sys.stdin.readline()[:-1].split(' '))

for c in range(n):
    
    # string?
    s = sys.stdin.readline()[:-1]

    # integer?
    k = int(sys.stdin.readline()[:-1])

    # list of integers
    # integer?
    tt = map(int, sys.stdin.readline()[:-1].split(' '))

exit()

abc = [chr(c) for c in range(65, 91)]
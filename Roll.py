import sys, random

cmd = sys.stdin.read()
if cmd == '/roll':
    print int(random.random() * 100)

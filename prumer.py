import sys
soucet = 0
delka = 0
args = sys.argv[1:] # skip arg 0
for arg in args:
    delka += 1
    soucet += float(arg)
prumer = soucet / delka
print(prumer)


import sys
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())
i=0
def natural():
    global i
    i=i+1
    print("hello",i)
    natural()
natural()f
def addUp(n, t=0):
    if n == 0:
        print(t)
    else:
        addUp(n-1, t+n)
        
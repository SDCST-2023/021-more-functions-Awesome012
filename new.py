def triangle(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    cool = [a,b,c]
    cool.sort()
    d = cool[0]
    e = cool[1]
    f = cool[2]
    if (d **2) + (e ** 2) == (f ** 2):
        return 2
    elif ((d ** 2) > (f ** 2) + (e ** 2) or (e ** 2) > (d ** 2) + (f ** 2) or (f ** 2) > (d ** 2) + (e ** 2)):
        return 3
    else:
        return 0

x = triangle(1,1,4)
print(x)
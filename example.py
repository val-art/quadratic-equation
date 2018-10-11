from math import sqrt

# a*x^2 + b*x + c = 0
a = input('A: ')
b = input('B: ')
c = input('C: ')

D = b ** 2 - 4 * a * c

if D == 0:
    x = -b / (2.0 * a)
    print "x = {}".format(x)
elif D > 0:
    x1 = (-b + sqrt(D)) / (2.0 * a)
    x2 = (-b - sqrt(D)) / (2.0 * a)
    print "x1 = {}".format(x1)
    print "x2 = {}".format(x2)
else:
    print "There is no real roots"
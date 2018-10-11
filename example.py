from cmath import sqrt
import sys

# a*x^2 + b*x + c = 0
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

# Some comment

D = b ** 2 - 4 * a * c

x1 = (-b + sqrt(D)) / (2.0 * a)
x2 = (-b - sqrt(D)) / (2.0 * a)
print "X1 = {}, X2 = {}".format(x1, x2)

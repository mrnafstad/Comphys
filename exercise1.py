import numpy as np
import matplotlib.pylab as mpl
n = 10
h = 1/float(n)
x = np.linspace(1,2,n)
der2 = np.zeros(n)
der3 = np.zeros(n)
func = np.arctan(x)

def derivative2pt(fpluss, f):
	der2pt = (fpluss - f)/h
	return der2pt

def derivative3pt(fpluss, fmin):
	der3pt = (fpluss - fmin)/float(2*h)
	return der3pt

for i in range(n-1):
	der2[i] = derivative2pt(func[i+1], func[i])
	if i >= 1:	
		der3[i] = derivative3pt(func[i+1], func[i-1])

mpl.plot(x, func)
mpl.hold("On")
mpl.plot(x, der2)
mpl.plot(x, der3)
mpl.show()
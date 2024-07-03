import numpy

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# x = stats.mode(speed)
# y = numpy.mean(speed)
# print(x)
# print(y)

""" Learn : median,mean, mode """


speeds = [32,111,138,28,59,77,97]

x = numpy.var(speeds)
y = numpy.std(speeds)
print(x)
print(y)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
xl = numpy.percentile(ages, 90)
print(xl)






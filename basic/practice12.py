# import numpy

# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# speed.sort()
# print(speed)

# x = numpy.median(speed)

# print(x)

str3 = "String"
print(str3.lower())

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)
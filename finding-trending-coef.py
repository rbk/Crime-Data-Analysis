import pandas, numpy
from sklearn import linear_model
import matplotlib.pyplot as plt


# California
# - Violent crime trending slightly down
# - Popuplation growing pretty fast

"""
Here is one way to get an increasing/decreasing trend:
>>> x = [12, 34, 29, 38, 34, 51, 29, 34, 47, 34, 55, 94, 68, 81]
>>> trend = [b - a for a, b in zip(x[::1], x[1::1])]
>>> trend
[22, -5, 9, -4, 17, -22, 5, 13, -13, 21, 39, -26, 13]
"""

ys = [
    31589000,
    31878000,
    32268000,
    32667000,
    33145121,
    33871648,
    34600463,
    35001986,
    35462712,
    35842038,
    36154147,
    36457549,
    36553215,
    36756666,
    36961664,
    37338198,
    37683933,
    37999878,
    38431393,
    38792291,
    38993940,
    39296476,
    39536653,
]
xs = numpy.array(range(0, len(ys))).reshape(-1, 1)

clf = linear_model.LinearRegression()
clf.fit(xs, ys)
# print(clf.score([[2018]], [636646]))

predictions_y = clf.predict(xs)
plt.plot(xs, predictions_y, color='blue', linewidth=3)

plt.scatter(xs, ys, color='black')
# print(len(xs))
# print(len(ys))
# print(xs)
print(ys)
print(clf.coef_)

plt.show()

# for year in range(2018, 2100):
#     prediction = clf.predict([[year]])
#     xs = numpy.append(xs, year)
#     ys.append(prediction)
#     print(year, prediction)
#     print(len(ys), len(xs))
#     clf.fit(numpy.array(xs).reshape(-1,1), ys)
# plt.scatter(xs, ys, color='black')
# plt.show()


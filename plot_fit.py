import numpy as np
from numpy.random import normal, random, uniform, lognormal
from numpy import histogram
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.stats import shapiro

# data = random(size=5000)
data = normal(loc=10, scale=1, size=500)
print shapiro(data)
# h, p = histogram(data, bins=10)

# Fit a normal distribution to the data:
mu, std = norm.fit(data)
print "mu = {0}, std = {1}".format(mu, std)
rsd = std/mu    # realtive standard deviation
print "rsd = {0}".format(rsd)
agreement_score = 1-rsd # agreement score
print "agreement_score = {0}".format(agreement_score)

# Plot the histogram.
plt.hist(data, bins=25, normed=True, alpha=0.5, color='g')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)
plt.show()

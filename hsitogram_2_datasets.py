import matplotlib.pyplot as plt

life_exp = [76,78,89,82,85,80]
life_exp_then = [45,57,32,49,62,53]

# Histogram of life_exp, 15 bins
plt.hist(life_exp, bins = 15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp_then, bins = 15)

# Show and clear plot again
plt.show()
plt.clf()
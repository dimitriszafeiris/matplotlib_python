import matplotlib.pyplot as plt

counter = [1,2,3,4,5,6,7,8,9,10]
amount = [50,55,60,45,37,80,52,37,20,60]

# Basic scatter plot, log scale
plt.scatter(counter, amount)
plt.xscale('log')

# Strings
xlab = 'Counter'
ylab = 'Total amount'
title = 'Total stats'

# Add axis labels
plt.xlabel(xlab) 
plt.ylabel(ylab)

# Add title
plt.title(title)


plt.show()
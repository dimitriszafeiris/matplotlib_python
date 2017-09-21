import matplotlib.pyplot as plt

counter = [100,200,300,400,500,600,700,800,900,1000]
amount = [50,55,60,45,37,80,52,37,20,60]

# Scatter plot
plt.scatter(counter, amount)

# Previous customizations
plt.xscale('log') 
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Stats')

# Definition of tick_val and tick_lab
tick_val = [1000,10000,100000]
tick_lab = ['1k','10k','100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# After customizing, display the plot
plt.show()
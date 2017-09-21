# Import numpy as np
import numpy as np
import matplotlib.pyplot as plt

counter = [100,200,300,400,500,600,700,800,900,1000]
amount = [50,55,60,45,37,80,52,37,20,60]

pop = [5,48,25,694,54,356,15,74,10,3]


# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(counter, amount, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Stats')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Additional customizations
plt.text(300, 63, 'A text')
plt.text(700, 49, 'B text')

# Add grid() call
plt.grid(True)


# Display the plot
plt.show()
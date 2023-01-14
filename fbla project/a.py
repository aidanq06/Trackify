import matplotlib.pyplot as plt

# Generate some data
x = [1, 2, 3, 4, 5]
y = [5, 7, 9, 11, 13]

# Create the plot
plt.plot(x, y)

# Label the x and y axes
plt.xlabel('value' + str(y))
plt.ylabel('value')

# Display the plot
plt.show()

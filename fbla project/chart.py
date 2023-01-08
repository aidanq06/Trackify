import matplotlib.pyplot as plt

# Define the data
data1 = [4, 2, 3, 1]
data2 = [1, 3, 2, 4]

# Create the chart
plt.bar(range(len(data1)), data1, label='Data 1')
plt.bar(range(len(data2)), data2, label='Data 2', bottom=data1)

# Customize the chart
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Data Chart')

# Add a legend
plt.legend()

# Show the chart
plt.show()

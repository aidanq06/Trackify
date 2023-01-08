import matplotlib.pyplot as plt
x_values = range(1, 11)
y_values = [5, 7, 3, 9, 2, 4, 8, 6, 1, 10]
y_labels = ["y_value " + str(x) for x in x_values]
plt.barh(y_labels, y_values)
plt.show()
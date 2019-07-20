import matplotlib.pyplot as plt

x_vals = list(range(1, 10001))
y_vals = [x**2 for x in x_vals]

plt.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Blues,
	edgecolor='none', s=30, alpha=1)

#set chart title & label axes
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

#set size of tick marks
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.show()
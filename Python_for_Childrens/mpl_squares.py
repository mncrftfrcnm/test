import matplotlib.pyplot as plt
plt.style.use('seaborn')
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
squares = [1, 4, 9, 16, 25]
squares2 = [8, 7, 9, 8, 26]
squares3 = [7, 6, 4, 5, 21]
input_values = [1, 2, 3, 4, 5]
fig, ax = plt.subplots()
#ax.plot(x_values, y_values, c='blue', linewidth=3)
ax.scatter(x_values, y_values, cmap=plt.cm.Blues, c='red', s=10)
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)
ax.tick_params(axis='both', labelsize=14)
plt.savefig('squares_plot.png', bbox_inches='tight')

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_facecolor('#99FFFF')
# Data for the bar graph
categories = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
values = [30.0000, 32.7778, 38.7700, 38.7780, 33.8889, 32.7778, 35.0000]

# Creating the bar graph
plt.bar(categories, values, color='#FF9900')

# Adding title and labels with larger font size
plt.title('Highest temperatures of the week in Mumbai', fontsize=12)
plt.xlabel('Days of the week', fontsize=10)
plt.ylabel('Temperature (ºC)', fontsize=10)

# Adding horizontal lines with labels for clarity
plt.axhline(y=25, color='#00FF00', linestyle='-', linewidth=3, label='Minimum Temperature')
plt.axhline(y=35, color='#FFFF00', linestyle='-', linewidth=3, label='Ideal Temperature')
plt.axhline(y=40, color='#FF0000', linestyle='-', linewidth=4, label='Maximum Temperature')

# Adjust font size globally
plt.rcParams.update({'font.size': 10})
# Change x-axis tick label font size
plt.xticks(fontsize=8.5)  # Adjust font size for x-axis labels
# Displaying legend
plt.legend()
# Display the graph
plt.show()

import matplotlib.pyplot as plt

# Create data
# y = [1, 2, 3, 4, 5]
# x = [2, 3, 5, 7, 11]

# # Create a plot
# # plt.plot(y, x)

# # Add labels and title
# plt.xlabel('THIS IS X')
# plt.ylabel('y')
# plt.title('Sample Plot')

# # Display the plot
# plt.show()


# ----------------------- [ Create a Line ] -----------------------


# # Define the data
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# temperatures = [10, 9, 8, 30, 6, 45 , 10, 25, 2, 1, 0, -1]  # Example temperatures decreasing over the year

# plt.plot(months, temperatures)
# # Add labels and title
# plt.xlabel('Month')
# plt.ylabel('Average Temperature (°C)')
# plt.title('Monthly Temperature Trend Over a Year')

# # Display the plot
# plt.show()

# ----------------------- [ Create a Line ] -----------------------


# Define the data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_revenue = [5000, 4800, 4600, 4500, 4300, 4200, 4100, 4000, 3900, 3600, 2000, 1000]  # Example sales revenue decreasing over the year

# Create a line plot
plt.figure(figsize=(7, 3))
plt.plot(months, sales_revenue, marker='o', linestyle='-', color="C2", label='Sales Revenue')

# Highlight the period of the lowest sales
min_sales_index = sales_revenue.index(min(sales_revenue))
plt.axvspan(months[min_sales_index], months[-1], color='blue', alpha=1, label='Lowest Sales Period')

# Add gridlines

# Annotate the highest and lowest sales
plt.annotate('Highest Sales', xy=(months[0], sales_revenue[0]), xytext=(months[0], sales_revenue[0] + 500),
             arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('Lowest Sales', xy=(months[min_sales_index], sales_revenue[min_sales_index]),
             xytext=(months[min_sales_index], sales_revenue[min_sales_index] - 500),
             arrowprops=dict(facecolor='red', shrink=0.05))

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Sales Revenue ($)')
plt.title('Monthly Sales Revenue Trend Over a Year')
plt.legend()

# Display the plot
plt.show()

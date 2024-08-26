import pandas as pd

# Create a DataFrame with names, cities, heights, and ages
data = {
    # Adding a None value for demonstration
    'names': ['Alice', 'Bob', 'Charlie', 'David', 'Bob'],
    'cities': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'heights': [5.5, 6.1, 5.8, 5.9, 5.6],  # Heights in feet
    'ages': [25, 30, 35, 40, 45]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Display the descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe(include='all'))  
# include='all' to include statistics for non-numeric columns
import matplotlib.pyplot as plt

# Data for grain exports rate of growth (y-axis) and years (x-axis)
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
growth_rates = [2.5, 3.2, 1.8, 4.5, 2.9, 3.7, 2.1, 2.8, 3.5, 3.2]

# Plotting the graph
plt.plot(years, growth_rates, marker='^', linestyle='-',color = "k")
plt.xlabel('Year')
plt.ylabel('Rate of Growth (%)')
plt.title('Grain Exports Rate of Growth in India (Last 10 Years)')

# Displaying the graph
plt.show()


#%%


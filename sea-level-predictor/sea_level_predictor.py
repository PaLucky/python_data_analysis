import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('./epa-sea-level.csv')
    # Create scatter plot
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
   
    print("slope: %f    intercept: %f" % (slope, intercept))

    years_extended = list(range(1880, 2050))
    line = [slope*xi + intercept for xi in years_extended]
    #years_extended =pd.date_range(start=1880, end=2050)
    #plt.plot(x, intercept + slope*x, 'r', label='fitted line')
    
    plt.scatter(x,y)
    xfuture = df[df['Year'] >= 2000]['Year']
    yfuture = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(xfuture, yfuture)
    years_extended2 = list(range(2000, 2050))
    line2 = [slope2*xi + intercept2 for xi in years_extended2]
    #plt.show()
    # Create first line of best fit    
    plt.plot(years_extended, line, color = 'green', label="1980-2055", linewidth=1)
    # Create second line of best fit
    plt.plot(years_extended2, line2, color = 'orange', label="2000-2050", linewidth=1)

    # Add labels and title
    #plt.legend()
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    scat=plt.scatter(x='Year',y='CSIRO Adjusted Sea Level',data=df)

    # Create first line of best fit

    res=linregress(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])

    ejeX=pd.Series(range(df['Year'].min(),2051))
    ejeY=res.slope *ejeX + res.intercept
    plt.plot(ejeX,ejeY)

    # Create second line of best fit

    res2=linregress(x=df[df['Year']>=2000]['Year'],y=df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])

    ejeX2=pd.Series(range(df[df['Year']>=2000]['Year'].min(),2051))
    ejeY2=res2.slope *ejeX2 + res2.intercept
    plt.plot(ejeX2,ejeY2)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
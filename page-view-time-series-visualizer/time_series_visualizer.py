import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def mapper(month):
   return month.strftime('%B')

def mapper2(year):
   return year.strftime('%Y')

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('./fcc-forum-pageviews.csv')
df.set_index('date')
#Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
df.date = pd.to_datetime(df["date"])

def draw_line_plot():
    print('df')
    fig, ax = plt.subplots(figsize=(28, 10))
    g=sns.lineplot(data=df, x='date', y='value')
    g.set(xlabel="Date", ylabel ="Page Views", title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    fig=g.figure
    #plt.show()
    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['Month'] = df['date'].apply(mapper)
    df['Years'] = df['date'].apply(mapper2)
    print(df)
    df_bar = df.copy()
    fig,ax = plt.subplots(figsize=(12, 12))
    # Draw bar plot
    g = sns.barplot(data=df_bar, x="Years", y="value", hue="Month",
     hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December'],ci=None, palette="muted")
    g.set(ylabel='Average Page Views')
    

    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    plt.figure( figsize=[10,5])
    plt.subplot(1, 2, 1)
    ax = sns.boxplot(x="Year", y="value", data=df_box)
    plt.subplot(1, 2, 2)
    ax2 = sns.boxplot(x="Month", y="value", data=df_box,
     order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec'])
    
    ax.set(ylabel='Page Views',title="Year-wise Box Plot (Trend)")
    ax2.set(ylabel='Page Views',title="Month-wise Box Plot (Seasonality)")
    plt.tight_layout()
    fig= plt.gcf()
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

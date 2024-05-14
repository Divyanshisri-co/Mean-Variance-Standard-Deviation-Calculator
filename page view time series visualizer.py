import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"]).set_index("date")

# Clean data
top_threshold = df['value'].quantile(0.975)
bottom_threshold = df['value'].quantile(0.025)

df = df[(df['value'] <= top_threshold) & (df['value'] >= bottom_threshold)]



def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    plot = ax.plot(df["value"])

    # Customize the plot (optional)
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df
    # Extract year and month from the 'date' column
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month

    # Create a pivot table to calculate average page views per month
    pivot_table = df.pivot_table(index='year', columns='month', values='value', aggfunc='mean')

    month_labels = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
    
    # Draw bar plot
    
    fig, ax = plt.subplots(figsize=(12, 6))
    pivot_table.plot(kind='bar', ax=ax)
    
    
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Daily Page Views per Month (2016-2019)')
    ax.set_xticklabels(df['year'].unique(), rotation=0)
    ax.set_xticks(range(len(df['year'].unique())))
    ax.legend(title='Months', labels=month_labels)



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
  
    

    # Draw box plots (using Seaborn)
    df_box["month_num"]=df_box["date"].dt.month
    df_box=df_box.sort_values("month_num")
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    
    
    # Plot Year-wise Box Plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    
    # Plot Month-wise Box Plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ])
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('./medical_examination.csv')

bmi = (df['weight'] / ((df['height']*0.01) ** 2))
# Add 'overweight' column
df.loc[bmi <= 25, 'overweight'] = 0
df.loc[bmi > 25, 'overweight'] = 1
df['overweight'] = df['overweight'].astype(int) 
#df['overweight'] = bmi


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])   

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    #df_cat = df_cat.drop_duplicates().reset_index(drop=True)

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(data=df_cat,kind = 'count', x="variable", hue="value", col="cardio")
    g.set_axis_labels("variable", "total")
    fig= g.fig

    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    correct_diastolic= df['ap_lo'] <= df['ap_hi']
    correct_height = df['height'] >= df['height'].quantile(0.025) 
    correct_height2 = df['height'] <= df['height'].quantile(0.975) 
    correct_weight = df['weight'] >= df['weight'].quantile(0.025) 
    correct_weight2 = df['weight'] <= df['weight'].quantile(0.975) 

    df_heat = df[correct_height2 & correct_weight2 & correct_height & correct_weight & correct_diastolic]

    #Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's heatmap(). Mask the upper triangle. The chart should look like "examples/Figure_2.png".

    # Calculate the correlation matrix
    corr = df_heat.corr()
    print(round(corr,1))

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones(corr.shape)).astype(np.bool)
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,mask=mask,linewidths=.5, annot=True, annot_kws={"fontsize":8},vmin=-0.1, vmax=0.24, center=0, fmt='.1f')
    #plt.show()

    fig.savefig('heatmap.png')
    return fig

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filepath = 'medical_examination.csv'

df = pd.read_csv(filepath)

# 2
# def bmi(height,weight):
#     bmi_value = weight/(height**2)
#     if bmi_value > 25:
#         return 1
#     else:
#         return 0
df['overweight'] = np.where(df['weight']/(np.square(df['height']/100))>25,1,0)

# 3
df['cholesterol'] = np.where(df['cholesterol']>1,1,0)
df['gluc'] = np.where(df['gluc']>1,1,0)
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])


    # 6
    df_cat = pd.melt(df,id_vars = 'cardio',value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
    df_cat = df_cat.groupby(['cardio','variable', 'value']).size().reset_index(name='total')
    # df_cat = df_cat.rename(columns={"variable":"feature"})

    # 7
    fig = sns.catplot(x = 'variable', y = 'total', hue = 'value',col = 'cardio', data = df_cat, kind = 'bar')

    # 8
    # fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & 
                     (df['height'] >= df['height'].quantile(0.025)) &
                     (df['height'] <= df['height'].quantile(0.975)) &
                     (df['weight'] >= df['weight'].quantile(0.025)) &
                     (df['weight'] <= df['weight'].quantile(0.975))                     
                     ]

    # 12
    corr = df_heat.corr().round(1)

    # 13
    mask = np.triu(np.ones_like(corr, dtype = bool))



    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, mask=mask, annot = True, cmap='coolwarm', square=True ,vmin = -0.1, vmax = 0.25)


    # 16
    fig.savefig('heatmap.png')
    return fig

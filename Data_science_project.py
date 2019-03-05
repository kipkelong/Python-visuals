import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;sns.set(font_scale=1.2)

#we will use seabon to plot

file ="/Users/shadrackkipkelong/Code/Average_Monthly_Price_of_Food_Crops_Commodities_Scheduled_Horticultural_Crops_between_2012_to_2015.xlsx" 
df = pd.read_excel(file,index=True)
df=df.dropna()
print(df.head())
sns.set_context("paper", font_scale=3, rc={"font.size":8,"axes.labelsize":10})
df_crops=df["Values_in_Ksh"]/df['Volume_in_Kgs']
df.insert(loc=5,column='Values_in_Ksh per KG', value=df_crops)
df=df.sort_values(by=['Values_in_Ksh per KG'],ascending=False)
pd.set_option('display.max_columns', 9)
print(df.sample(15))

#plot of crops under various crop varieties eg legumes,cereals etc
sns.set_style('whitegrid')
ax=sns.swarmplot(x="Produce_Variety", y=("Values_in_Ksh per KG"), data=df)
ax.set_title("Produce_Variety Price Variation")
ax.set(xlabel ='Commodity Type', ylabel ='Values in Ksh per KG')
ax.set_xticklabels(ax.get_xticklabels(),rotation=60,fontsize=15)
ax.set_xlabel("Produce Variety",fontsize=10)
ax.set_ylabel("Values in Ksh per KG",fontsize=10)
plt.legend()
plt.show()

#plot of crops prices over the 4 year period

ax=sns.stripplot(x="Commodity_Type", y=("Values_in_Ksh per KG"), data=df)
ax.set_title("Price of Food Crops Horticultural Crops between 2012-2015")
ax.set(xlabel ='Commodity Type', ylabel ='Values in_Ksh per KG')
ax.set_xticklabels(ax.get_xticklabels(),rotation=90,fontsize=10)
ax.set_xlabel("Commodity Type",fontsize=20)
ax.set_ylabel("Values in Ksh per KG",fontsize=20)
plt.legend()
plt.show()
print(df.describe)



Data_science_project.py

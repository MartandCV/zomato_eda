# zomato_eda
Exploratory data analysis on Zomato data set to make some observations.

# In Data Analysis What all things do we do
 1. Missing Values
 2. Explore about the numberical values
 3. Explore about the categorical values
 4. Finding relationship between features

# Some important functions for EDA
1. df.head()
2. df.columns
3. df.info()
4. df.describe()
5. df.isnull().sum()
6. [features for features in df.columns if df[features].isnull().sum()>0]
7. sns.heatmap(df.isnull(),yticklabels=False,cbar=False)
8. final_df = pd.merge(df, df_country, on='Country Code', how='left')
9. final_df.Country.value_counts()
10. plt.pie(country_val[:3], labels = country_names[:3],autopct='%1.2f%%')
11. final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})
12. sns.barplot(x='Aggregate rating', y='Rating Count',data=ratings)

## Note Data set available on Kaggle and also uploaded in repo

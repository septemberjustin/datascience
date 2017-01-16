import numpy as np
import pandas as pd

# pd.Series?

# animals = ['Tiger', 'Bear', 'Moose']
# print pd.Series(animals)

# numbers = [1, 2, 3]
# print pd.Series(numbers)

# animals = ['Tiger', 'Bear', None]
# print pd.Series(animals)

# numbers = [1, 2, None]
# print pd.Series(numbers)


# print np.nan == None
# print np.nan == np.nan
# print np.isnan(np.nan)

# sports = {'Archery': 'Bhutan', 'Golf': 'Scotland', 'Sumo': 'Japan', 'Taekwondo': 'South Korea'}
# s = pd.Series(sports)
# print s
# print s.index

# s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
# print s

# sports = {'Archery': 'Bhutan', 'Golf': 'Scotland', 'Sumo': 'Japan', 'Taekwondo': 'South Korea'}
# s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
# print s

# sports = {'Archery': 'Bhutan', 'Golf': 'Scotland', 'Sumo': 'Japan', 'Taekwondo': 'South Korea'}
# s = pd.Series(sports)
# print s

# print s.iloc[3]
# print s.loc['Golf']
# print s[3]
# print s['Golf']

# sports = {99: 'Bhutan', 100: 'Scotland', 101: 'Japan', 102: 'South Korea'}
# s = pd.Series(sports)
# print s.iloc[0]

# s = pd.Series([100.00, 120.00, 101.00, 3.00])
# print s

# total = 0
# for item in s:
# 	total+=item
# print(total)

# total = np.sum(s)
# print(total)

# s = pd.Series(np.random.randint(0,1000,10000))
# s.head()
# len(s)

# %%timeit -n 100
# summary = 0
# for item in s:
# 	summary+=item

# s = pd.Series([1, 2, 3])
# s.loc['Animal'] = 'Bears'
# print s

# original_sports = pd.Series({'Archery': 'Bhutan', 'Golf': 'Scotland', 'Sumo': 'Japan', 'Taekwondo': 'South Korea'})
# cricket_loving_countries = pd.Series(['Austrilia', 'Barbados', 'Pakistan', 'England'], index=['Cricket', 'Cricket', 'Cricket', 'Cricket'])
# all_countries = original_sports.append(cricket_loving_countries)
# print all_countries
# print all_countries.loc['Cricket']

# purchase_1 = pd.Series({'Name': 'Chris', 'Item Purchased': 'Dog Food', 'Cost': 22.50})
# purchase_2 = pd.Series({'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50})
# purchase_3 = pd.Series({'Name': 'Vinod', 'Item Purchased': 'Bird Seed', 'Cost': 5.00})
# df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
# print df.head()
# print df.loc['Store 1']
# print type(df.loc['Store 1'])
# print df.T
# print df.T.loc['Cost']  
# print df['Cost']   #type are different 
# print df.loc['Store 1']['Cost']
# print df.loc[:,['Name', 'Cost']]
# print df.drop('Store 1')
# print df

# copy_df = df.copy()
# copy_df = copy_df.drop('Store 1')

# del copy_df['Name']
# # print copy_df

# df['Location'] = None
# print df

# df = pd.read_csv('olympic.csv', index_col = 0, skiprows=1)
# print df.head()
# print df.columns

# for col in df.columns:
# 	if col[:2] == '01':
# 		df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
# 	if col[:2] == '02':
# 		df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
# 	if col[:2] == '03':
# 		df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
# 	if col[:1] == '\xe2':
# 		df.rename(columns={col:'#' + col[1:]}, inplace=True)

# print df['Gold'] > 0
# only_gold = df.where(df['Gold'] > 0)
# print only_gold.head()
# print only_gold.count()
# print df['Gold'].count()
# only_gold = only_gold.dropna()
# print only_gold.head()

# only_gold = df[df['Gold'] > 0]
# print only_gold.head()

# print len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)])
# print df[ (df['Gold.1'] > 0) & (df['Gold'] == 0)]

# df['country'] = df.index
# df = df.set_index('Gold')
# print df.head()

# df = df.reset_index()
# print df.head()

df = pd.read_csv('census.csv')
# print df.head()

# print df['SUMLEV'].unique()
df = df[df['SUMLEV'] == 50]
# print df.head()

columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
df = df.set_index(['STNAME', 'CTYNAME'])
# df.loc['Michigan', 'Washtenaw County']
print df.loc[ [('Michigan', 'Washtenaw County'), ('Michigan', 'Wayne County')] ]
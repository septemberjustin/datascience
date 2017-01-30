# print(pd.merge(products, invoices, left_index=True, right_on='Product ID'))

# print(df.drop(df[df['Quantity'] == 0].index).rename(columns={'Weight': 'Weight (oz.)'}))

# print(df.groupby('Category').agg('sum'))

#########
# print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))

# Or alternatively without using a lambda:
# def totalweight(df, w, q):
#        return sum(df[w] * df[q])
#        
# print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))

#########
# s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])

# s.astype('category', categories=['Low', 'Medium', 'High'], ordered=True)



#########
# s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])

# pd.cut(s, 3)

# You can also add labels for the sizes [Small < Medium < Large].
# pd.cut(s, 3, labels=['Small', 'Medium', 'Large'])

#########
# print(pd.pivot_table(Bikes, index=['Manufacturer','Bike Type']))


###Merging Dataframes
import pandas as pd
import numpy as np

# df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
# 	                {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
# 	                {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
# 	                index=['Store 1', 'Store 1', 'Store 2'])

# df['Date'] = ['December 1', 'January 1', 'mid-May']
# df['Delivered'] = True
# df['Feedback'] = ['Positive', None, 'Negative']

# adf = df.reset_index()
# adf['Date'] = pd.Series({0: 'December 1', 2: 'mid-May'})

# staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
# 	                     {'Name': 'Sally', 'Role': 'Course liasion'},
# 	                     {'Name': 'James', 'Role': 'Grader'}])
# staff_df = staff_df.set_index('Name')

# student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
# 	                     {'Name': 'Mike', 'School': 'Law'},
# 	                     {'Name': 'Sally', 'School': 'Engineering'}])
# student_df = student_df.set_index('Name')

# print(staff_df.head())
# print
# print(student_df.head())

# print pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)

# print pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)

# print pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)

# print pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)

# staff_df = staff_df.reset_index()
# student_df = student_df.reset_index()
# print pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')

# staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
# 	                     {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
#                          {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
# student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
#                            {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
#                            {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
# print pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')

# staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
#                          {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
#                          {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])

# student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
#                            {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
#                            {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
# print staff_df
# print student_df
# print pd.merge(staff_df, student_df, how='inner', left_on=['First Name', 'Last Name'], right_on=['First Name', 'Last Name'])


##### Idiomatic Pandas: Making Code Pandorable

# df = pd.read_csv('census.csv')
# print df
# print (df.where(df['SUMLEV']==50).dropna().set_index(['STNAME','CTYNAME']).rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}).head())
# df = df[df['SUMLEV']==50]
# df.set_index(['STNAME','CTYNAME'], inplace=True)
# df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})

# rows = ['POPESTIMATE2010',
#         'POPESTIMATE2011',
#         'POPESTIMATE2012',
#         'POPESTIMATE2013',
#         'POPESTIMATE2014',
#         'POPESTIMATE2015']
# print df.apply(lambda x: np.max(x[rows]), axis=1)


##### Group by
# df = pd.read_csv('census.csv')
# df = df[df['SUMLEV']==50]
# print df

# %%timeit -n 10
# for state in df['STNAME'].unique():
# 	avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
# 	print('Counties in state ' + state + ' have an average population of ' + str(avg))

# for group, frame in df.groupby('STNAME'):
# 	avg = np.average(frame['CENSUS2010POP'])
# 	print('Counties in state ' + group + ' have an average population of ' + str(avg))

# print df.head()
# df = df.set_index('STNAME')

# def fun(item):
# 	if item[0]<'M':
# 		return 0
# 	if item[0]<'Q':
# 		return 1
# 	return 2

# for group, frame in df.groupby(fun):
# 	print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')

# print df.groupby('STNAME').agg({'CENSUS2010POP': np.average})
# print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']))
# print(type(df.groupby(level=0)['POPESTIMATE2010']))

# print(df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg':np.average, 'sum': np.sum}))

# print(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011'].agg({'avg': np.average, 'sum': np.sum}))

# print(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011'].agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))


#### Scales

# df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'], 
# 	              index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
# df.rename(columns={0: 'Grades'}, inplace=True)
# df['Grades'].astype('category')

# grades = df['Grades'].astype('category', 
# 	                         categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
# 	                         ordered=True)
# print grades>'C'

# df = pd.read_csv('census.csv')
# df = df[df['SUMLEV']==50]
# df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
# print pd.cut(df['avg'],10)

#### Pivot Tables
# df = pd.read_csv('cars.csv')
# print df.head()
# print df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)
# print df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)

##### Date Functionality in Pandas
# print pd.Timestamp('9/1/2016 10:05AM')

# t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
# print t1

d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
print ts3





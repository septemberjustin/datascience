# print(pd.merge(products, invoices, left_index=True, right_on='Product ID'))

# print(df.drop(df[df['Quantity'] == 0].index).rename(columns={'Weight': 'Weight (oz.)'}))

# print(df.groupby('Category').agg('sum'))

#########
print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))

# Or alternatively without using a lambda:
# def totalweight(df, w, q):
#        return sum(df[w] * df[q])
#        
# print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))

#########
s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])

s.astype('category', categories=['Low', 'Medium', 'High'], ordered=True)



#########
s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])

pd.cut(s, 3)

# You can also add labels for the sizes [Small < Medium < Large].
pd.cut(s, 3, labels=['Small', 'Medium', 'Large'])

#########
print(pd.pivot_table(Bikes, index=['Manufacturer','Bike Type']))
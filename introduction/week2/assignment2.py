#answer one
def answer_one():
    df.sort(['Gold'], inplace=True, ascending=False)
    return df.iloc[0].name
answer_one()

#answer two
def answer_two():
    df['Diff'] = df['Gold'] - df['Gold.1']
    df.sort(['Diff'], inplace=True, ascending=False)
    return df.iloc[0].name
answer_two()

#answer three
def answer_three():
    new_df = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)]
    new_df['Diff2'] = (new_df['Gold'] - new_df['Gold.1']) / new_df['Gold.2']
    new_df.sort(['Diff2'], inplace=True, ascending=False)
    return new_df.iloc[0].name
answer_three()

#answer four
def answer_four():
    df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']*1
    return df['Points']
answer_four()

#answer five
def answer_five():
    return census_df.groupby('STNAME')['CTYNAME'].size().argmax()
answer_five()

#answer six
def answer_six():
    return census_df.groupby('STNAME')['CENSUS2010POP'].max().nlargest(3).index.tolist()
answer_six()

#answer seven
def answer_seven():
    df = census_df[(census_df['SUMLEV'] == 50)].set_index('CTYNAME')
    df['maxpop'] = df[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].max(axis=1)
    df['minpop'] = df[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].min(axis=1)
    df['Diff'] = df['maxpop'] - df['minpop']
    df.sort(['Diff'], inplace=True, ascending=False)
    return df.iloc[0].name
answer_seven()

#answer eight
def answer_eight():
    df = census_df[((census_df['REGION'] == 1) | (census_df['REGION'] == 2)) & (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014']) & (census_df['CTYNAME'].str.startswith('Washington'))]
    columns_to_keep = ['STNAME', 'CTYNAME']
    df = df[columns_to_keep]
    df.sort(inplace=True, ascending=True)
    return df
answer_eight()
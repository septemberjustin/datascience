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
#     df = census_df[census_df['SUMLEV'] == 50]
#     df = df.set_index(['STNAME', 'CTYNAME'])
#     df = df.groupby('STNAME')
#     df['size'] = df.size()
    return census_df.groupby('STNAME')['CTYNAME'].size().argmax()
answer_five()
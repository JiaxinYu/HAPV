def select_columns(df, columnname, cnum=16):
  clist1 = pd.DataFrame(df.columns.to_list(), columns=['cname'])
  k_column = clist1[clist1['cname'] == columnname].index[0]
  return df.iloc[:, (k_column+1):(k_column+1+cnum)]
  

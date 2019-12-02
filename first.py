import pandas as pd

print('Example path: ./example_data.xlsx')
adp = pd.read_excel(input('Please input the path of the ADP spreadsheet:').replace('\\','/'), usecols = ['EMPLOYEE TAX ID','PLAN NAME','COVERAGE LEVEL VALUE'])
cigna = pd.read_excel(input('Please input the path of the Cigna spreadsheet:').replace('\\','/'), usecols = ['Subscriber Id','Billing Line Desc','Tier'])
adp.columns = ['SSN','Plan Name','Coverage Level']
cigna.columns = ['SSN','Plan Name','Coverage Level']
cigna.dropna(inplace=True)
df1_1 = adp.append(cigna)
df1_2 = df1_1.append(cigna)
df1_3 = df1_2.drop_duplicates(keep=False)
df2_1 = cigna.append(adp)
df2_2 = df2_1.append(adp)
df2_3 = df2_2.drop_duplicates(keep=False)
print(df1_3)
print('\n','=====================','\n')
print(df2_3)
while not (input('Please input "Done" to exit: ') == 'Done'):
    pass

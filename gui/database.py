import pandas as pd

file_path = r'C:\Users\migue\OneDrive\Área de Trabalho\Miguel\Programming\FinanceManager\FinanceManagerAccounts.xlsx'

excelFile = pd.ExcelFile(file_path, engine='openpyxl')
accountsData = pd.read_excel(file_path, sheet_name='accounts-data', engine='openpyxl')

transactionsNumber = accountsData.iloc[0, 7]
formatted_transactionsNumber = str(transactionsNumber).zfill(4)

transactionsData = pd.read_excel(file_path, sheet_name=str(formatted_transactionsNumber), engine='openpyxl')

print(transactionsData.head())
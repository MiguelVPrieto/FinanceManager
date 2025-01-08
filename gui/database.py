import pandas as pd

file_path = r'C:\Users\migue\OneDrive\Área de Trabalho\Miguel\Programming\FinanceManager\FinanceManagerAccounts.xlsx'

excelFile = pd.ExcelFile(file_path, engine='openpyxl')
accountsData = pd.read_excel(file_path, sheet_name='accounts-data', engine='openpyxl')

def loadTransactions(accountId):
    transactionsID = accountsData.iloc[accountId, 7]
    formattedTransactionsID = str(transactionsID).zfill(4)
    transactionsData = pd.read_excel(file_path, sheet_name=str(formattedTransactionsID), engine='openpyxl')
    return transactionsData

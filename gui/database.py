import pandas as pd
import hashlib

database = r'C:\Users\migue\OneDrive\Área de Trabalho\Miguel\Programming\FinanceManager\FinanceManagerAccounts.xlsx'

def loadDatabase():
    return pd.read_excel(database, sheet_name='accounts-data', engine='openpyxl')

def loadTransactions(accountId):
    accountsData = loadDatabase()
    transactionsID = accountsData.iloc[accountId, 6]
    formattedTransactionsID = str(transactionsID).zfill(4)
    transactionsData = pd.read_excel(database, sheet_name=str(formattedTransactionsID), engine='openpyxl')
    return transactionsData

def loginAuth(fullName, password):
    accountsData = loadDatabase()
    match = accountsData[(accountsData['account_name'] == fullName) & (accountsData['password'] == password)]

    if not match.empty:
        accountId = match.index[0]
        return accountId
    else:
        return -1
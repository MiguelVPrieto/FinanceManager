import pandas as pd

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

def createAuth(fullName):
    accountsData = loadDatabase()
    match = accountsData[(accountsData['account_name'] == fullName)]

    if not match.empty:
        return -1
    else:
        return 0

def create(fullName, balance, password):
    accountsData = loadDatabase()
    length = accountsData.shape[0]
    accountID = accountsData.iloc[length-1, 0]+1
    email = "N/A"
    numTrans = 0
    transPageID = str(accountID).zfill(4)

    if createAuth(fullName) == -1:
        return -1

    try:
        newAccount = pd.DataFrame([{
            'account_id': accountID,
            'account_name': fullName,
            'password': password,
            'email': email,
            'balance': int(balance),
            'number_transactions': numTrans,
            'transactions_page_id': int(transPageID),
        }])

        accountsData = pd.concat([accountsData, newAccount], ignore_index=True)

        with pd.ExcelWriter(database, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            accountsData.to_excel(writer, sheet_name='accounts-data', index=False)

            transactions_df = pd.DataFrame(columns=['transaction_number', 'I/E', 'amount', 'category', 'date', 'time', 'sender', 'receiver', 'notes'])
            transactions_df.to_excel(writer, sheet_name=transPageID, index=False)

        return 0
    except:
        return -2
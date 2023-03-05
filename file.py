import openpyxl as xl

accountSummaryHeading = ['Account Number', 'Account Type', 'Bank Name', 'IFSC', 'Status']
profileHeading = ['Name', 'Date of Birth', 'Mobile', 'Address', 'Email', 'PAN']
transactionHeading = ['Type', 'Account', 'Transaction Date', 'Narration']
file = 'DataStore.xlsx'


def createDataStore(accountSummaryHeading=None, profileHeading=None, transactionHeading=None):
    # check if file already exists
    try:
        wb = xl.load_workbook(file)
        ws = wb.worksheets[0]  # select first worksheet
    except FileNotFoundError:
        # create a workbook
        workbook = xl.Workbook()
        # create different sheets to store the data
        accountSummarySheet = workbook.active
        accountSummarySheet.title = 'Account Summary'
        profileSheet = workbook.create_sheet(title='Profiles')
        transactionSheet = workbook.create_sheet(title='Transactions')
        # write data heading rows
        accountSummarySheet.append(accountSummaryHeading)
        profileSheet.append(profileHeading)
        transactionSheet.append(transactionHeading)
        workbook.save(file)

if __name__ == '__main__':
    createDataStore(accountSummaryHeading, profileHeading, transactionHeading)

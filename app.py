import json

from flask import Flask, request

import file

app = Flask(__name__)
app.config["DEBUG"] = True

file = 'DataStore.xlsx'

accountSummaryHeading = ['Account Number', 'Account Type', 'Bank Name', 'IFSC', 'Status']
profileHeading = ['Name', 'Date of Birth', 'Mobile', 'Address', 'Email', 'PAN']
transactionHeading = ['Type', 'Account', 'Transaction Date', 'Narration']

single_input_json = {
    "accountSummaries":
        {
            "accountNumber": "123123123",
            "accountType": "Deposit",
            "bankName": "sbi",
            "IFSC": "sbin0000",
            "status": "Active"
        },
    "profiles":
        {
            "name": "asdf",
            "dob": "2345",
            "mobile": "0000000000",
            "address": "asdfasdf",
            "email": "asdf@asdf.com",
            "pan": "1231231231"
        },

    "transactions":
        {
            "type": "DEBIT",
            "amount": "Deposit",
            "txnDate": "23232323",
            "narration": "asdfasdfadsfasd"
        }

}

@app.route('/')
def hello_world():
    return '''<h1>Ingest data</h1>
    <p>A prototype API for reading and storing data. Look at the readme for different endpoints</p>'''

@app.route('/add', methods=['POST'])
def addDetails():
    details = json.loads(request.data)
    # ingest values to excel sheet
    file.addValuesToExcel(details['accountSummaries'], 'Account Summary')
    file.addValuesToExcel(details['profiles'], 'Profiles')
    file.addValuesToExcel(details['transactions'], 'Transactions')
    # return message to user
    return "Details added successfully"

if __name__ == '__main__':
    app.run()

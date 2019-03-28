import csv
import json
import os
import random
import uuid
from datetime import timedelta, date

import settings
from object.Bank import Bank
from object.Branch import Branch, ATM
from object.Product import Product
from object.Transaction import generate_transaction
from object.User import User

if __name__ == '__main__':
    user1 = next(User.Generator(1, 'male'))
    user2 = next(User.Generator(1, 'female'))

    user_list = [user1, user2]
    bank_number = 3
    bank_list = []

    branch_list = []
    branch_number = 4
    atm_list = []
    atm_number = 6
    product_list = []
    product_number = 10
    bankGenerator  = Bank.Generator(bank_number)
    for i in range(bank_number):
        bank = next(bankGenerator)
        bank_list.append(bank)
        branchGenerator = Branch.Generator(bank, branch_number)
        atmGenerator  = ATM.Generator(bank, atm_number)
        productGenerator = Product.Generator(bank, product_number)
        for j in range(branch_number):
            branch_list.append(next(branchGenerator))
        for j in range(atm_number):
            atm_list.append(next(atmGenerator))
        for j in range(product_number):
            product_list.append(next(productGenerator))

    account_list = []
    branch_tmp = random.choice(branch_list)
    account1 = user1.create_account(branch_tmp, "CURRENT", "MXN", 60000)
    user1.create_customer(branch_tmp.bank, )

    account1.set_behavior(income=33000)
    account_list.append(account1)
    branch_tmp = random.choice(branch_list)
    account2 = user1.create_account(branch_tmp, "SAVING", "MXN", 2000000)
    account2.set_behavior(income=30000)
    account_list.append(account2)

    branch_tmp = random.choice(branch_list)
    account3 = user2.create_account(branch_tmp, "SAVING", "MXN", 600000)
    account3.set_behavior(income=20000)
    account_list.append(account3)

    branch_tmp = random.choice(branch_list)
    account4 = user2.create_account(branch_tmp, "CURRENT", "MXN", 150000)
    account4.set_behavior(income=60000,
    spending_frequency =
    { "food":          6,
      "utility":       2,
      "clothing":      2,
      "auto":          0,
      "health":        0,
      "entertainment": 3,
      "gift":          2,
      "education":     1,
      "fee":           3 }
    , housing_type = {
        "RENT":-20000
    })
    account_list.append(account4)


    months = 36
    date_start = date.today() - timedelta(days = months*30)
    transaction_list = []
    for i in range(months):
        date_start = date_start + timedelta(days= 30)
        for account in account_list:
            transaction_list.extend(account.generateTransaction(date_start))



    with open("transaction.csv", 'w') as csv_file:
        fnames = ['id', 'bank','counterparty','posted','new_balance','value','type', 'user', 'account_type']
        #wr = csv.DictWriter(csv_file, fieldnames=fnames, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #wr.writeheader()
        wr= csv.writer(csv_file, delimiter=',')
        wr.writerow(fnames)
        for transaction in transaction_list:
            wr.writerow([
                transaction.id,
                transaction.this_account.branch.bank.id,
                transaction.other_counterparty,
                str(transaction.posted),
                transaction.new_balance,
                '{:.2f}'.format(transaction.value),
                transaction.type,
                transaction.this_account.user[0].username,
                transaction.this_account.type
                         ])
            '''
            wr.writerow({
                "id" : transaction.id,
                "bank": transaction.this_account.branch.bank.id,
                "counterparty": transaction.other_counterparty,
                "posted": str(transaction.posted),
                "new_balance": transaction.new_balance,
                "value": '{:.2f}'.format(transaction.value),
                "type": transaction.type,
                "user": transaction.this_account.user[0].username,
                "account_type": transaction.this_account.type
            })
            '''

    try:
        os.makedirs(settings.OUTPUT_PATH)
    except:
        pass
    with open('{}sandbox_pretty.json'.format(settings.OUTPUT_PATH), 'w') as outfile:
        json.dump({
            "users": user_list,
            "banks": bank_list,
            #"branches": branch_list,
            "accounts":account_list,
            #"atms":atm_list,
            #"counterparties":counterparty_list,
            #"products":product_list,
            "transactions":transaction_list
        }, outfile, default=lambda x:x.dict(), indent=4)

    #with open('{}customers_pretty.json'.format(settings.OUTPUT_PATH), 'w') as outfile:
    #    json.dump(customer_list, outfile, default=lambda x:x.dict, indent = 4)
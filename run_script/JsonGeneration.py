import json
import itertools
import os
import uuid
import random

import settings

from object.Account import Account
from object.Bank import Bank
from object.Branch import Branch, ATM
from object.Counterparty import Counterparty
from object.Customer import Customer
from object.Product import Product
from object.Routing import top_merchants
from object.Transaction import Transaction
from object.User import User, mails

if __name__ == '__main__':
    user_number = 10
    user_list = []
    userGenerator = User.Generator(user_number)
    for i in range(user_number):
        user_list.append(next(userGenerator))

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

    transactions_num = 5
    transactions_list = []
    for user in user_list:
        branch_selected = random.choice(branch_list)
        account = next(Account.Generator(1, branch_selected, user))
        account_list.append(account)

        transactionsGenerator = Transaction.Generator(account, 12)
        transactions_list.extend(next(transactionsGenerator))

    customer_list= []
    for bank, user in itertools.product(bank_list, user_list):
        customer = next(Customer.Generator(user, bank, 1))
        customer_list.append(customer)

    try:
        os.makedirs(settings.OUTPUT_PATH)
    except:
        pass
    with open('{}sandbox_pretty.json'.format(settings.OUTPUT_PATH), 'w') as outfile:
        json.dump({
            "users": user_list,
            "banks": bank_list,
            "branches": branch_list,
            "accounts":account_list,
            "atms":atm_list,
            #"counterparties":counterparty_list,
            "products":product_list,
            "transactions":transactions_list
        }, outfile, default=lambda x:x.dict, indent=4)

    with open('{}customers_pretty.json'.format(settings.OUTPUT_PATH), 'w') as outfile:
        json.dump(customer_list, outfile, default=lambda x:x.dict, indent = 4)
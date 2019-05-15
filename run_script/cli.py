import click
import csv
import json
import os
import random
import re
import numpy as np
from datetime import timedelta, date
from openpyxl import load_workbook

import settings
from object.Bank import Bank
from object.Branch import Branch, ATM
from object.Product import Product
from object.User import User

@click.group()
def cli():
    pass

@cli.command(help="Generate Main Json file")
@click.option('--input_file', default="./input_file/info.xlsx", required=False, help='Filename of first name')
@click.option('--output_dir', default='./output_path/', help='first name to be fill to dataset')
def generate_main_file(input_file, output_dir):
    user_list = User.generator_for_file(settings.OPTIONS_PATH)
    bank_number = int(os.getenv('BANK_NUMBER'))

    currency = os.getenv('COUNTRY')
    branch_list = []
    branch_number = int(os.getenv('BRANCH_NUMBER'))
    atm_list = []
    atm_number = int(os.getenv('ATM_NUMBER'))
    product_list = []
    product_number = int(os.getenv('PRODUCT_NUMBER'))
    bank_list = Bank.generate_from_file(bank_number)
    for bank in bank_list:
        branch_list.extend(Branch.generate_from_file(bank, branch_number))
        atm_list.extend(ATM.generate_from_file(bank, atm_number))
        product_list.extend(Product.generate_from_file(bank, product_number))

    account_list = []
    for user in user_list:
        branch_tmp = random.choice(branch_list)
        account1 = user.create_account(branch_tmp, "CURRENT", user.country, user.current)
        account1.set_behavior(income=user.current, spending_frequency =
            { "food":          user.food,
              "utility":       user.utility,
              "clothing":      user.clothing,
              "auto":          user.auto,
              "health":        user.health,
              "entertainment": user.entertainment,
              "gift":         user.gift,
              "education":     user.education,
              "fee":           user.fee },
            housing_type={
                "RENT": -user.rent
            } if user.rent > 0 else None
        )
        account_list.append(account1)

        branch_tmp = random.choice(branch_list)
        account2 = user.create_account(branch_tmp, "SAVING", user.country, user.savings)
        account2.set_behavior(income=user.savings)
        account_list.append(account2)

    months = 36
    date_start = date.today() - timedelta(days=months * 30)
    transaction_list = []
    for i in range(months):
        date_start = date_start + timedelta(days=30)
        for account in account_list:
            transaction_list.extend(account.generateTransaction(date_start))

    with open("transaction.csv", 'w') as csv_file:
        fnames = ['id', 'bank', 'counterparty', 'posted', 'new_balance', 'value', 'type', 'user', 'account_type']
        # wr = csv.DictWriter(csv_file, fieldnames=fnames, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # wr.writeheader()
        wr = csv.writer(csv_file, delimiter=',')
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


    output_dir = int(os.getenv('OUTPUT_DIR'))
    try:
        os.makedirs(output_dir)
    except:
        pass
    with open('{}sandbox_pretty.json'.format(output_dir), 'w') as outfile:
        json.dump({
            "users": user_list,
            "banks": bank_list,
            "branches": branch_list,
            "accounts": account_list,
            "atms":atm_list,
            # "counterparties":counterparty_list,
            "products":product_list,
            "transactions": transaction_list
        }, outfile, default=lambda x: x.dict(), indent=4)

    customer_list = []
    for user in user_list:
        for bank in bank_list:
            customer_list.append(user.create_customer(bank))

    with open('{}customers_pretty.json'.format(output_dir), 'w') as outfile:
        json.dump(customer_list, outfile, default=lambda x: x.dict(), indent=4)


@cli.command(help="Generate Counterparty Json file")
@click.option('--input_file', default="./input_file/OBP_counterparties_TESOBE_Hong_Kong.xlsx", required=True, help='Filename of first name')
@click.option('--city', default="Hong Kong", required=True, help='Filename of first name')
@click.option('--output_dir', default="./output_path/", help='first name to be fill to dataset')
def generate_counterparty_file(input_file, city, output_dir):
    wb = load_workbook(input_file)

    sheet_selected = [sheetname for sheetname in wb.sheetnames if city in sheetname ]

    import pandas as pd

    dataframe = pd.read_excel(input_file, sheet_name = sheet_selected, header=None, index_col=None, skiprows=3)

    df = pd.DataFrame()
    for i, j in dataframe.items():
        df = pd.DataFrame(j)

    df.columns= ['type', 'name', 'reference', 'value', 'frequency', 'logo','homepage']

    df.type = df["type"].apply(lambda x: re.split('_|/',x)[0].lower())
    #df.frequency = df["frequency"].apply(lambda x: str("0") if x is np.nan else frequecy_mapping[x.lower()])

    df = pd.DataFrame({
        "type":df["type"].apply(lambda x: re.split('_|/',x)[0].lower()),
        "name" : df["name"],
        #"value" : df["value"],
        #"frequency" : df["frequency"].apply(lambda x: str("0") if x is np.nan else frequecy_mapping[x.lower()]),
        "logo" : df["logo"],
        "homepage" : df["homepage"]
    })

    df_list = []
    for i, rows in df.iterrows():
        df_list.append({
            "name":rows['name'],
            "category":rows['type'],
            "superCategory":rows['type'],
            "logoUrl":rows['logo'] if rows['logo'] is not np.nan else "",
            "homePageUrl":rows['homepage'] if rows['homepage'] is not np.nan else "",
            "region":city
        })

    with open('{}counterparty_pretty.json'.format(output_dir), 'w') as outfile:
        json.dump(df_list, outfile, default=lambda x: x.dict(), indent=4)

@cli.command(help="init")
@click.option('--bank_number', default=3, help='bank_number')
@click.option('--branch_number', default=4, help='branch_number')
@click.option('--atm_number', default=6, help='atm_number')
@click.option('--product_number', default=10, help='product_number')
@click.option('--country', default='MXN', help='country')
@click.option('--output_dir', default='../output_path', help='output_dir')
def init(bank_number, branch_number, atm_number, product_number, country, output_dir):
    os.environ['BANK_NUMBER'] = str(bank_number)
    os.environ['BRANCH_NUMBER'] = str(branch_number)
    os.environ['ATM_NUMBER'] = str(atm_number)
    os.environ['PRODUCT_NUMBER'] = str(product_number)
    os.environ['COUNTRY']=country
    os.environ['OUTPUT_DIR']=output_dir
    click.echo('{}'.format(os.getenv('BANK_NUMBER', False)))

@cli.command(help="web_init")
@click.option('--api_host', default='http://127.0.0.1:8080', help='api_host')
@click.option('--redirect_url', default='http://127.0.0.1:9090', help='redirect_url')
@click.option('--admin_username', default='pflee', help='admin_username')
@click.option('--admin_password', default='Pflee@0218', help='admin_password')
@click.option('--file_root', default='G:/OBP-Project/SandboxDataGenerator/output_path', help='file_root')
def web_init(api_host, redirect_url, admin_username, admin_password, file_root):
    os.environ['API_HOST'] = str(api_host)
    os.environ['REDIRECT_URL'] = str(redirect_url)
    os.environ['ADMIN_USERNAME'] = str(admin_username)
    os.environ['ADMIN_PASSWORD'] = str(admin_password)
    os.environ['OUTPUT_DIR']=file_root
    click.echo('{}'.format(os.getenv('ADMIN_USERNAME', False)))

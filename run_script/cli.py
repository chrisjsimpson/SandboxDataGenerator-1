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
        account1.set_behavior(income=33000)
        account_list.append(account1)
        branch_tmp = random.choice(branch_list)
        account2 = user.create_account(branch_tmp, "SAVING", user.country, user.savings)
        account2.set_behavior(income=30000)
        account_list.append(account2)

    click.echo([user.dict() for user in user_list])

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
def init(bank_number, branch_number, atm_number, product_number):
    os.environ['BANK_NUMBER'] = str(bank_number)
    os.environ['BRANCH_NUMBER'] = str(branch_number)
    os.environ['ATM_NUMBER'] = str(atm_number)
    os.environ['PRODUCT_NUMBER'] = str(product_number)
    os.environ['COUNTRY']='MXN'
    click.echo('{}'.format(os.getenv('BANK_NUMBER', False)))
'''
@cli.command(help="add first name")
@click.option('--filename', default="firstname.csv", required=False, help='Filename of first name')
@click.option('--firstname', prompt='First Name', help='first name to be fill to dataset')
@click.option('--gender', default = 'Male', prompt='Gender', help='name to gender')
def add_firstname(filename = "firstname.csv", firstname='', gender='Male' ):
    if firstname != '':
        fields=[firstname, gender]
        with open(filename,'a') as file:
            writer = csv.writer(file)
            writer.writerow(fields)

@cli.command(help="add last name")
@click.option('--filename', default="lastname.csv", required=False, help='Filename of last name')
@click.option('--lastname', prompt='Your name', help='last name to be fill to dataset')
def add_lastname(filename = "lastname.csv", lastname = ''):
    fields=[lastname]
    with open(filename, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(fields)

@cli.command(help="add user")
@click.option('--filename', default="", help='Number of greetings.')
def add_behavior(filename = None, counterparty_name = '', frequency = 1, value = 0):
    click.echo("add user")
'''
if __name__=='__main__':
    init()
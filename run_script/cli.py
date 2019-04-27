import click
import csv

@click.group()
def cli():
    pass

@cli.command(help="init")
def init():
    click.echo("init")

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

@cli.command(help="add email")
def add_email(filename = None):
    click.echo("add user")

@cli.command(help="")
def add
if __name__=='__main__':
    init()
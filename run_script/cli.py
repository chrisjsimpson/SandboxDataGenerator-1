import click

@click.group()
def cli():
    pass

@cli.command(help="init")
def init():
    click.echo("init")

@cli.command(help="")
def adduser():
    click.echo("add user")


cli.add_command(init)
cli.add_command(adduser)

if __name__=='__main__':
    init()
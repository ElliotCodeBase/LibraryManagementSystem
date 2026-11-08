from rich.table import Table
from rich.console import Console
from rich import box
from rich import print

CreationState = False
console = Console()



def AcountCreation(CreationState):
    while CreationState:
        pass


def logo():
    Logo = r"""
    [bold purple]██████  ██ ██████   ██████   ██████  ██   ██
    ██   ██ ██ ██   ██ ██    ██ ██    ██ ██  ██
    ██████  ██ ██████  ██    ██ ██    ██ █████
    ██   ██ ██ ██   ██ ██    ██ ██    ██ ██  ██
    ██████  ██ ██████   ██████   ██████  ██   ██[/bold purple]
    """
    print(" "*10, Logo)
logo()

table = Table(
    title="[bold cyan]Library Book Inventory[/bold cyan]",
    box=box.ROUNDED,  # Rounded borders
    border_style="bright_blue",

)

table.add_column("Name")
table.add_column("Name")
table.add_column("Name")
table.add_column("Name")
table.add_column("Name")

console.print(table)






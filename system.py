from rich.table import Table
from rich.console import Console
from rich import box
from rich import print

import os
import sys
import time

CreationState = False
UserlogState = False

console = Console()

def logo():
    Logo = r"""
    [purple]██████  ██ ██████   ██████   ██████  ██   ██
    ██   ██ ██ ██   ██ ██    ██ ██    ██ ██  ██
    ██████  ██ ██████  ██    ██ ██    ██ █████
    ██   ██ ██ ██   ██ ██    ██ ██    ██ ██  ██
    ██████  ██ ██████   ██████   ██████  ██   ██[/purple]
    """
    print(Logo)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def AcountCreation(CreationState):
    while CreationState:
        pass

def LoginSignUp(UserLogState):

    while UserLogState:
        logo()
        UserInput = input("Log in[1]\nSign out[2]\n")
        if UserInput == "1":
            print("Logged in")
            break
        elif UserInput == "2":
            print("Sign in")
            break
        else:
            clear()
            print("TRY AGAIN")
            time.sleep(1)


LoginSignUp(True)

clear()
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






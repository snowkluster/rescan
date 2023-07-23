#!/usr/bin/env python3

import typer
from rich import print
from rich.console import Console
import dns.resolver
import dns.reversename
import dns.zone
import dns.exception
import threading
import socket

console = Console()
app = typer.Typer(help=console.print("Made By [green]SnowKluster[/green]"))
err_console = Console(stderr=True)

@app.command()
def scan(ip: str):
    console.print(f"Scanning IP Address: [green]{ip}[/green]")

@app.command()
def dns():
    print("Deleting user: Hiro Hamada")

if __name__ == "__main__":
    app()
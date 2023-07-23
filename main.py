#!/usr/bin/env python3

import typer
from rich import print
from rich.console import Console
from rich.progress import track
import dns.resolver
import dns.reversename
import dns.zone
import dns.exception
from threading import Thread
import socket
import sys

console = Console()
app = typer.Typer(help=console.print("Made By [red]SnowKluster[/red]"))
typer.Typer(help=console.print("Github: [light-blue]https://github.com/snowkluster[/light-blue]"))
err_console = Console(stderr=True)

@app.command()
def scan(ip: str,start_port: int = typer.Argument(0),end_port: int = typer.Argument(65535)):
    console.print(f"Scanning IP Address: [green]{ip}[green]")
    console.print(f"Starting port scan from [green]{start_port}[/green] till [green]{end_port}[/green]")
    ports = prepare_port(start_port,end_port)
    scan_port(ip,ports)
    threading()

@app.command()
def recon(domain: str):
    console.print(f"Domain for recon : [green]{domain}[/green]")

@app.command()
def version():
    console.print("[purple]rescan version 1.0[/purple]")

def scan_port(ip,ports):
    open_ports = []
    with typer.progressbar(ports) as port:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s = socket.socket()
            s.settimeout(1)
            port = next(ports)
            result = s.connect_ex((ip,port))
            if result == 0:
                open_ports.append(port)
            s.close()
            console.print(f"[purple]{open_ports}[/purple]\n")
        except(ConnectionRefusedError):
            console.print("[red]Connection refused by host [/red]")
            console.print_exception(show_locals=False)
            sys.exit()

def threading(threads=20):
    thread_list = []
    for _ in range(threads+1):
        thread_list.append(Thread(target=scan_port))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

def prepare_port(sport,eport):
    for ports in range(sport,eport):
        yield ports

if __name__ == "__main__":
    app()
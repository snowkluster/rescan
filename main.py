#!/usr/bin/env python3

import typer
from rich import print
from rich.console import Console
from rich.progress import track
from threading import Thread
import socket
import sys

console = Console()
app = typer.Typer(help=console.print("Made By SnowKluster"))
typer.Typer(help=console.print("Github: [light-blue]https://github.com/snowkluster[/light-blue]"))
err_console = Console(stderr=True)

@app.command()
def scan(ip: str,start_port: int = typer.Argument(0),end_port: int = typer.Argument(65535)):
    console.print(f"Scanning IP Address: [green]{ip}[green]")
    if (start_port and end_port):
        console.print(f"Starting port scan from [green]{start_port}[/green] till [green]{end_port}[/green]")
    console.print("Scanning all ports")
    ports = prepare_port(start_port,end_port)
    threading(ip,ports)

@app.command()
def version():
    console.print("[purple]rescan version 1.0[/purple]")

@app.command()
def info():
    console.print("the program defaults to 60 threads, pass number of threads you want to you use to change it")
    console.print("for more info checkout the project github")

def scan_port(ip,ports):
    for port in  ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s = socket.socket()
            s.settimeout(1)
            result = s.connect_ex((ip,port))
            if result == 0:
                console.print(f"open port: {port}")
            s.close()
        except(ConnectionRefusedError):
            console.print("[red]Connection refused by host [/red]")
            console.print_exception(show_locals=False)
            sys.exit()

def threading(ip,port,threads=60):
    thread_list = []
    for _ in range(threads+1):
        thread_list.append(Thread(target=scan_port,args=(ip,port)))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

def prepare_port(sport,eport):
    for ports in range(sport,eport):
        yield ports

if __name__ == "__main__":
    app()
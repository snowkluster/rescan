#!/usr/bin/env python3

import typer
from rich import print
from rich.console import Console
from rich.progress import track
from threading import Thread
import signal
import socket
import sys

console = Console()
app = typer.Typer(help=console.print("Made By [blue]SnowKluster[/blue]"))
typer.Typer(help=console.print("Github: [light-blue]https://github.com/snowkluster[/light-blue]"))
err_console = Console(stderr=True)

@app.command()
def scan(ip: str,num_threads: int,start_port: int = typer.Argument(0),end_port: int = typer.Argument(65535)):
    console.print(f"Scanning IP Address: [green]{ip}[green]")
    if (start_port and end_port):
        console.print(f"Starting port scan from [green]{start_port}[/green] till [green]{end_port}[/green]")
    console.print("Scanning all ports with default Config")
    if (num_threads):
        console.print(f"Starting scan with {num_threads} threads")
    ports = prepare_port(start_port,end_port+1)
    threading(ip,ports,threads=num_threads)

@app.command()
def version():
    console.print("[purple]rescan version 1.0[/purple]")

@app.command()
def info():
    console.print("the program defaults to 60 threads, pass number of threads you want to you use to change it")
    console.print("for more info checkout the project github")

def scan_port(ip,ports):
    quitting = False
    if quitting:
        sys.exit("Exitting Program")
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
        thread.daemon=True
        thread.start()
    for thread in thread_list:
        thread.join()

def signal_handler(signal, frame):
    print("exiting")
    sys.exit(0)

def prepare_port(sport,eport):
    for ports in range(sport,eport):
        yield ports


def main():
    app()
    signal.signal(signal.SIGINT, signal_handler)
if __name__ == "__main__":
    main()
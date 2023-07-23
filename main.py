#!/usr/bin/env python3

import typer
import dns.resolver
import dns.reversename
import dns.zone
import dns.exception
import threading
import socket

app = typer.Typer()

@app.command()
def scan(ip: str):
    print(f"scanning ip address: str({ip})")

@app.command()
def delete():
    print("Deleting user: Hiro Hamada")

if __name__ == "__main__":
    app()
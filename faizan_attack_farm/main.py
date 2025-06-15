# main.py
# Project: Faizan™ DDoS Attack Farm - v1.0
# Author: Faizan™ Mughal
# License: MIT

from interface.cli import launch_interface

def banner():
    print(r"""
███████╗ █████╗ ██╗███████╗ █████╗ ███╗   ██╗
██╔════╝██╔══██╗██║██╔════╝██╔══██╗████╗  ██║
███████╗███████║██║█████╗  ███████║██╔██╗ ██║
╚════██║██╔══██║██║██╔══╝  ██╔══██║██║╚██╗██║
███████║██║  ██║██║██║     ██║  ██║██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝
        ⚔ Faizan™ DDoS Attack Farm ⚔
""")

if __name__ == "__main__":
    banner()
    launch_interface()

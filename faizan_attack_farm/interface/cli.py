# interface/cli.py
def launch_interface():
    print("\n[+] Welcome to Faizan™ Attack Farm CLI\n")
    print("1. UDP Flood")
    print("2. SYN Flood")
    print("3. HTTP Flood")
    print("4. Slowloris Attack")
    print("0. Exit")

    choice = input("\n[?] Select attack type: ")

    if choice == "1":
        from bots.udp_flood import start_udp
        start_udp()
    elif choice == "2":
        from bots.syn_flood import start_syn
        start_syn()
    elif choice == "3":
        from bots.http_flood import start_http
        start_http()
    elif choice == "4":
        from bots.slowloris import start_slowloris
        start_slowloris()
    else:
        print("Exiting... Shukriya, Faizan™")

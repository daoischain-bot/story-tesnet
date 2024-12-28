import random
import time
import pyfiglet
from web3 import Web3
from colorama import Fore, Style, init

init(autoreset=True)
a1 = pyfiglet.figlet_format("DAOISCHAIN")
print(Fore.GREEN + Style.BRIGHT + a1)
print("--------------------------------------------------------------")
print("Story Odyssy Protocol Testnet Auto Send")
print(Fore.BLUE + Style.BRIGHT + "Telegram Channel: https://t.me/newtesnet")
print(Fore.GREEN + Style.BRIGHT + "Donate: 0x73725bD6684346cBf841cbFb6b7FC5be6B627f98")
print("--------------------------------------------------------------")

a2 = 'https://odyssey.storyrpc.io'
a3 = 1516
a4 = Web3(Web3.HTTPProvider(a2))

if not a4.is_connected():
    print("Unable to connect to the RPC server")
    exit()

with open('sender.txt', 'r') as f1:
    a5 = f1.readline().strip()
    a6 = f1.readline().strip()

with open('receivers.txt', 'r') as f2:
    a7 = [line.strip() for line in f2.readlines()]

a5 = a4.to_checksum_address(a5)

print(Fore.BLUE + "Sender wallet address: " + a5)

while True:
    a8 = input("Do you want to send a fixed amount or random amount? (fixed/random): ").strip().lower()
    if a8 == 'fixed':
        a9 = float(input("Enter the amount to be sent: "))
        a10 = a11 = a9
        break
    elif a8 == 'random':
        a10 = float(input("Enter the minimum amount to be sent: "))
        a11 = float(input("Enter the maximum amount to be sent: "))
        break
    else:
        print("Invalid choice. Please enter 'fixed' or 'random'.")

try:
    while True:
        a12 = a4.eth.get_balance(a5)
        print(Fore.BLUE + "Account balance: " + f"{a4.from_wei(a12, 'ether')} IP")

        if a8 == 'fixed':
            a9 = a10
        else:
            a9 = random.uniform(a10, a11)
        
        a13 = a4.to_wei(a9, 'ether')

        a14 = random.uniform(1.01, 1.10)
        a15 = {
            'to': a4.to_checksum_address(random.choice(a7)),
            'value': a13,
            'gasPrice': int(a4.eth.gas_price * a14),
            'nonce': a4.eth.get_transaction_count(a5),
            'chainId': a3
        }

        a16 = a4.eth.estimate_gas(a15)
        a15['gas'] = a16

        a17 = a16 * a15['gasPrice']
        a18 = a13 + a17

        print(Fore.BLUE + "Total sent: " + f"{a4.from_wei(a18, 'ether')} IP")
        print(Fore.BLUE + "Total gas fee: " + f"{a4.from_wei(a17, 'ether')} IP")

        if a12 < a18:
            print("Insufficient balance to cover gas fee and transaction value.")
            break

        a19 = a15['to']
        print(Fore.YELLOW + "Recipient wallet address: " + a19)

        a20 = a4.eth.account.sign_transaction(a15, a6)
        a21 = a4.eth.send_raw_transaction(a20.raw_transaction)

        print(Fore.MAGENTA + "Transaction sent successfully with hash: " + a21.hex())

        a22 = random.randint(5 * 60, 10 * 60)
        for a23 in range(a22, 0, -1):
            a24, a25 = divmod(a23, 3600)
            a26, a27 = divmod(a25, 60)
            print(f"Waiting time remaining: {a24} hours {a26} minutes {a27} seconds", end='\r')
            time.sleep(1)
        print()

except KeyboardInterrupt:
    print("Transaction sending stopped by user.")

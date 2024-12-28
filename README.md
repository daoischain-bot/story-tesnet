This **Story Odyssey Protocol Tesnet** script can perform automatic transfers within a time range of 12 to 24 hours. Additionally, this script will also perform random token transfers with a range of token amounts that can be specified.

install > Use Python 3.10.12

- git clone https://github.com/daoischain-bot/story-tesnet.git
- pip install web3
- pip install colorama
- pip install requests
- pip install pyfiglet

• Edit sender.txt add address and private key

• Edit receiver.txt add target address

Done all and Run with python3 bot.py

1. To minimize a script running on a VPS without stopping it you can use **tmux**
- sudo apt install tmux
- tmux -S mysession
- python3 your_script.py
  
2. Detach from the screen session (without stopping the script): Press Ctrl + B, then D
3. Reattach to the screen session (when you want to check on your script):
- tmux attach -t mysession
4. Stoping script press Ctrl + c
  
**Donate: 0x73725bd6684346cbf841cbfb6b7fc5be6b627f98**

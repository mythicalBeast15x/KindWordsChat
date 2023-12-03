# KindWordsChat Report
### Goal
There were 4 main goals of this project:
- Create a safe place where students, or anyone could talk about things that trouble them.
- Censor any harmful or derogatory words that would cause any student to feel unwelcome
- Allow anyone on a local network to connect to the chat
### Significance
This project allows people over a network to share their feelings and talk in a place that makes everyone feel welcome. 
The filter censors any words that would cause people to feel as if they do not belong. This allows it to form a safe space for members who join. 
Members can join and leave at any time and can create a username to protect their identity. It is on a network so that groups can join and feel more connected
### Installation Instructions
##### Server Instructions
1. Download the repository file (Make sure that the generateHash.py, profanities.pkl, and server.py are in the same directory
2. Make sure that the socket, threading, and zeroconf packages are installed on your device (Using an IDE will usually help with this)
3. In a terminal window, navagate to the KindWordsChat directory
4. call python server.py

##### Client Instructions
1. On a computer not running the server file, download the repository or just the client.py file
2. Make sure the following packages are installed on your computer: socket, threading, tkinter, and zeroconf
3. In the terminal, navagate to the KindWordsChat directory
4. call python client.py


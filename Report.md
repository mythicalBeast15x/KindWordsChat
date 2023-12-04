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
5. Disclaimer: Using the server on the same computer as the client can lead to bugs. It's easier to use different devices for the client and server

### Code Structure
#### Diagram
<div align="center">
  <img src="https://github.com/mythicalBeast15x/KindWordsChat/blob/main/KindWordsChat%20Diagram.jpg">
  <br>
 </div>
 
#### Explanation
- The server.py file opens a port and starts listening.
- It uses the zeroconf library to find the public and private ip address.
- The client.py file uses the same library to find the port. Then it connects to the server.
- The server sends the client a list of all the taken usernames so the user can't choose a name already chosen
- Once the user enters their name, the client adds the connection to the list
- When the user sends a message, it goes to the server. Before the server broadcasts it to all the users, it checks each word in the hashtable. If It passes, it sends the message. If a word is in the hashtable, it is censored with astricks like this ****.
- The generateHash.py file is the hashtable class. It reads in an already loaded hashtable so that it doesn't have to be created on every startup of the server
- The hashtable is set up by taking a word and storing it as a key in a dictonary. The value is equal to the current index of the hashtable list. The hashtable list then appends the word
- The hash function works by trying to access the dictionary value of the word. If the key does not exist it returns false. If the key does exist, then it checks the index of the hashtable list. If that matches the word, it returns true and the server censors that word
  
### Functionality and Test Results
#### Connecting to Server
- When the client first connects to the server, it notifies the client that it successfully connects and broadcasts that the user has joined
<div align="center">
  <img src="https://github.com/mythicalBeast15x/KindWordsChat/blob/main/testing_pics/testing1.jpg">
  <br>
 </div>

#### Sending Messages to Other Users
- You can send and recieve messages to other users. You will see you message with your name in barckets like so [your_name]: message. You will see other people's message in the same format
<div align="center">
  <img src="https://github.com/mythicalBeast15x/KindWordsChat/blob/main/testing_pics/testing2.jpg">
  <br>
 </div>
 <div align="center">
  <img src="https://github.com/mythicalBeast15x/KindWordsChat/blob/main/testing_pics/testing3.jpg">
  <br>
 </div>
 <div align="center">
  <img src="https://github.com/mythicalBeast15x/KindWordsChat/blob/main/testing_pics/testing4.jpg">
  <br>
 </div>

#### Other Users Disconnecting
- Users can disconnect from the server at any time. A message will send to everyone letting them know that the user disconnected
<div align="center">
  <img src="https://github.com/mythicalBeast15x/KindWordsChat/blob/main/testing_pics/testing6.jpg">
  <br>
 </div>

 #### Censoring Words
 - When bad words are detected. They will be censored and replaced by astericks.
<div align="center">
  <img src="https://github.com/mythicalBeast15x/KindWordsChat/blob/main/testing_pics/testing8.jpg">
  <br>
 </div>
 <div align="center">
  <img src="https://github.com/mythicalBeast15x/KindWordsChat/blob/main/testing_pics/testing9.jpg">
  <br>
 </div>

### Discussion and Conclusion
#### Issues
- Connecting to the network was very difficult. There are many factors that go into this. You have to broadcast on a specific server, and other programs that want to connect with it have to look for it
- Beacuse this program can handle multiple users, it has to use threading. Getting all of the threads to work together and wait was a big hurdle in this project.
- I'm not entirely sure why, but using the client and server on the same device causes errors, but only sometimes. Sometimes it works, but sometimes it acts weird.

#### Limitations
- There weren't many places to get the profanity lists. I guess people don't want to have lists of bad words

#### Applied Learning from the Course
- Something on my mind this entire project was the time complexity. I enjoy reducing the time complexity of my programs, and this was no exception. The problem for this project was seeing if a word was in a list of prohibited words. The easiest solution would be to just put them all in a list and iterate over each one every time. That would leave it's complexity to O(n). This isn't the worst for this project which only has about 500 banned words. But if you wanted to scale it up it would start to slow things down. My second thought was to use something like a tree, or mergesort to cut the search in half. That would be O(nlogn) and would be faster, but using a hashtable would be O(1).
- Using strings with hashmaps are kind of tricky. Because encoding a string to a reasonable integer value is hard. I chose to go a slightly easier route. I stored the words in a dictionary, with each value being the key's index in a list of the words. This way, all I have to do is see if the word is in the dictionary, get it's index and check if they match. The only problem I ran into was finding the key in the dictionary. But I avoided that by using the .get() function. It returns None if the key does not exist, allowing me to not iterate over the keys.

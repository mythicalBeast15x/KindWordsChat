# Chat Room Filter
### Team: Love-Divine Onwulata and Charles Langley
## Description
This project is a chat room that will allow those on the same network to send messages to each other in a chatroom. The core of the project is the chat filter. It will allow people to send messages, however if there is an explicit word in the message it will censor the message. If there are too many expletives in the sentence, it will not send the message. To do this we will use a Hash Table. We will encode a list of common expletives with a hash function, then store them in the hash table. When the message is entered, it will parse the string, and if the word is in the table, it will censor it.

We hope to implement NLP into the project and block messages that are deemed unsafe, however the project is big enough as is

The goals of this project is to:

  - Create a chat that people on the network can connect to and chat
    * Use C++ and sockets to connect to other devices and send messages
  - Create a filter that can censor words from the message
    * Use a hash table to store harmful words

If there is time:
- Block messages if they contain negative sentiment
- Use NLP on the messages to detect negative or harmful sentiment

# Bots
There are two Different applications in this project.
### 1. signalWireDiscord.py
### 2. python in.py and python out.py



## SignalWire Bots description

### 1. signalWireDiscord.py
The bot gets the latest messages from signalwire and posts them in a specified discord chat.
It does this by checking for new messages in your signalwire account every few minutes.
The user can also give commands to bot for sending texts messages through discord.

### 2. python in.py and python out.py
in.py: uses relay Api. Doesnt have to constantly ping signal wire. Signal Wire pushes the message onto this client on its own.
out.py: similar to signalWireDiscord.py's ability to read commands through discord and send outgoing msgs.

### What you need
> Server/ PC running python3.6 minimum

> install necessary libraries using pip (signalwire, discord.py)

> Edit/customize the SignalWireDiscord.py file on lines 7,8,18,33,62, 96

Run using
```bash
python signalWireDiscord.py
```
Or
```bash
python in.py &
python out.py &
```

### Commands
#### signalWireDiscord.py
The following commands can be made by user with id in line 33, just by typing in a channel with the bot.
Note that the bot will reply on channel with id in line 96.

> hello
:Quick check if Bot is able to read your messages.

> refresh
:checks signalwire for any new messages

> help
:Tries to help

> cancel
:Cancels  text message you were about to send

> num ___________
replace the blank with phone number you want to send message to. 
Message after this that the bot reads will be the body of the text message, which gets sent as soon as recieved.

#### in.py out.py
 Coming soon

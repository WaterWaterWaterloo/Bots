# Bots

## SignalWire Bots
The bot gets the latest messages from signalwire and posts them in a specified discord chat.
The user can also give commands to bot for sending texts messages through discord.


### What you need
> Server/ PC running python3.6 minimum

> install necessary libraries using pip (signalwire, discord.py)

> Edit/customize the SignalWireDiscord.py file on lines 7,8,18,33,62, 96

Run using
```bash
python signalWireDiscord.py
```

### Commands
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


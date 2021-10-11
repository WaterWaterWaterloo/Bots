import discord
from discord.ext import tasks
from signalwire.rest import Client as signalwire_client
from datetime import datetime
import pytz

sclient = signalwire_client("PROJECT ID", "api token", signalwire_space_url = 'space url')
TOKEN = 'discordBotToken' 
lastmessege = '93cl9a0'# Parameter for checking last message posted

client = discord.Client()

state = 0 # if 1, next message in chat is messages body
messagelist = []
today = datetime.utcnow()


est = pytz.timezone('US/Eastern')

@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))
    myLoop.start()

@client.event
async def on_message(message):
    global state
   
    global messagelist
    if message.author == client.user:
        return
    
    if message.author.id != your Discord ID HERE :
        return

    if message.content.lower() == 'hello':
        await message.channel.send(f'Hello!!, {message.author.display_name}!')
        return
    if message.content.lower() == 'refresh':
        await message.channel.send(f'Refreshed')
        myLoop.restart()
        return
    if message.content.lower() == 'help':
        await message.channel.send(f'type num _______, and then body time')
        return
    if message.content.lower() == 'cancel':
        await message.channel.send(f'cancelled')
        state = 0     
        messagelist = []
        return

    msgbody = message.content.lower().split()
    if(msgbody):
        if(msgbody[0] == 'num' and len(msgbody) ==2): # we got the num command, store the TO number, 
            messagelist.append(msgbody[1])
            state = 1 # next call is expected to be msg body
            await message.channel.send(f'write body')
            return

    if(state ==1 and messagelist): # state is 1, this  is body of text msg
        sclient.messages.create(
                              from_='ur signalwire phone number',
                              body=message.content, # Dont forget +1 before #
                              to=messagelist[0]
                          )
        myLoop.restart()

        state = 0
        return
    

@tasks.loop(minutes = 15) # repeat after every 15 minutes
async def myLoop():
    global lastmessege
 
    global today
    
    messages=[]

    if(datetime.utcnow().date() > today.date()):     # make sure messages sent in the last few minutes of the day dont get missed
        messages  = sclient.messages.list(date_sent=today)
        today = datetime.utcnow().date()
    else:
        messages  = sclient.messages.list(date_sent=today)

    mylist = []
    for msg in messages:
        if(lastmessege == msg.sid):
            break
        else:
            mylist.insert(0,msg)

    if(mylist):
        for a in mylist:
            await client.wait_until_ready()
            discch = client.get_channel(int(channel id where u want to post incoming messages))
            await discch.send(a.date_created.astimezone(est).strftime("%m/%d/%Y, %H:%M:%S") + "|" + a.direction + "|" + a.from_ + "|" + "\n" + a.body)
        lastmessege=mylist.pop().sid
            


client.run(TOKEN)

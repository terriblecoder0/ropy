from ropy import Client


key = ".ROBLOSECURITY_KEY_GOES_HERE"
client = Client(security_key=key,)


@client.events.listen("ready")
async def on_ready():
    print("Ready!")



@client.events.listen("close")
async def on_close():
    print("Closed!")



client.login()








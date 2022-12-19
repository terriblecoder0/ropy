from ropy import Client


key = ".ROBLOSECURITY TOKEN GOES HERE"


client = Client(security_key=key,)



@client.events.listen(event="ready")
async def on_ready():
    print("Ready!")



@client.events.listen(event="close")
async def on_ready():
    print("Closed!")



client.login()








import os
import verify
import asyncio
from events import Events




class Client:

    def __init__(self, security_key: str, poll_interval = 60):
        os.environ["security_key"] = security_key
        self.poll_interval = poll_interval
        self.events = Events(events=["ready", "close", "inbound"])

    def login(self):

        success, result = verify.get_auth_user()
        if success:
            asyncio.run(self.events.invoke(event="ready"))
        else:
            asyncio.run(self.events.invoke(event="close"))





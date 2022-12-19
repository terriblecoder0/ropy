import os
import verify
import asyncio
from events import Events




loop = asyncio.get_event_loop()


class Client:

    def __init__(self, security_key: str, poll_interval = 60):
        os.environ["security_key"] = security_key
        self.poll_interval = poll_interval
        self.events = Events(events=["ready", "close", "inbound"])

    def login(self):

        ok, result = verify.get_auth_user()
        if ok:
            loop.run_until_complete(self.events.invoke("ready"))
        else:
            loop.run_until_complete(self.events.invoke("close"))





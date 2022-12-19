







class Events:

    def __init__(self, events: list):
        self.__events = events
        self.__listeners = []

    def listen(self, event: str):
        
        if not event in self.__events:
            raise Exception(f"{event} is not a valid event name")

        def add_listener(f):
            self.__listeners.append([event, f])
            return f
        
        return add_listener


    async def invoke(self, event: str, *args):
        for l in self.__listeners:
            if l[0] == event:
                await l[1](*args)
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json

class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        # Called on connection and is about to finish the websocket handshake.
        print("Websocket connected...", event)
        self.send({
            'type': 'websocket.accept'
        })

    # def websocket_receive(self, event):
    #     # Called when data is received from the client
    #     print("Message received...", event['text'])
    #     for i in range(10):
    #         self.send({
    #         'type': 'websocket.send',
    #         'text': str(i)
    #         })
    #         sleep(1)
    def websocket_receive(self, event):
        print("Message received...", event)
        print(json.loads(event['text']))                   # Converting str to dict using 'json.loads'
        for i in range(10):
            self.send({
            'type': 'websocket.send',
            'text': json.dumps({"count":i})                # Converting dict to str using 'json.dumps' 
            })
            sleep(1)

    def websocket_disconnect(self, event):
        # Called when the socket closes
        print("Websocket disconnected...", event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        # Called on connection and is about to finish the websocket handshake.
        print("Websocket connected...", event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        # Called when data is received from the client
        print("Message received...", event)
        print("Messaged is:", event['text'])
        for i in range(15):
            await self.send({
            'type': 'websocket.send',
            'text': str(i)
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        # Called when the socket closes
        print("Websocket disconnected...", event)
        raise StopConsumer()
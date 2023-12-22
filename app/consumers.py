from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        # Called on connection.
        print("Websocket connected...", event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        # Called when data is received from the client
        print("Message received...", event)
        print("Messaged is:", event['text'])

    def websocket_disconnect(self, event):
        # Called when the socket closes
        print("Websocket disconnected...", event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        # Called on connection.
        print("Websocket connected...", event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        # Called when data is received from the client
        print("Message received...", event)
        print("Messaged is:", event['text'])

    async def websocket_disconnect(self, event):
        # Called when the socket closes
        print("Websocket disconnected...", event)
        raise StopConsumer()
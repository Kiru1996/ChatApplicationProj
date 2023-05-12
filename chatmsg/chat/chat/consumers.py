import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """
    This consumer handles websocket connections for a chat room.

    Attributes:
    - roomGroupName (str): the name of the chat room group.

    Methods:
    - connect(): Adds the channel to the chat room group and accepts the websocket connection.
    - disconnect(close_code): Removes the channel from the chat room group when the connection is closed.
    - receive(text_data): Receives a message from a connected client and broadcasts it to all other clients in the chat room.
    - sendMessage(event): Sends a message to the connected client.

    Example usage:
    - Create an instance of this consumer and route websocket connections to it in your Django Channels routing file.
    """

    async def connect(self):
        """
        Adds the channel to the chat room group and accepts the websocket connection.
        """
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        """
        Removes the channel from the chat room group when the connection is closed.
        """
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_layer
        )

    async def receive(self, text_data):
        """
        Receives a message from a connected client and broadcasts it to all other clients in the chat room.
        """
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "username": username,
            })

    async def sendMessage(self, event):
        """
        Sends a message to the connected client.
        """
        message = event["message"]
        username = event["username"]
        await self.send(text_data=json.dumps({"message": message, "username": username}))

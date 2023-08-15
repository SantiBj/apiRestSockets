from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Customer
import json

#como 
class customerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("hola")
        await self.accept()

        #añadiendo a un grupo
        await self.channel_layer.group_add('customer',self.channel_name)

    async def disconnect(self, code):
        print("chao")
        #saliendo del grupo
        await self.channel_layer.group_discard('customer',self.channel_name)

    async def newCustomer(self,event):
        print(event)
        data = event['data']
        #consult
        await self.send(
            text_data = json.dumps({
                "type":"newCustomer",
                "customer":data
            })
        )
from motor.motor_asyncio import AsyncIOMotorClient

class DatabaseConnect:
    def __init__(self):
        self.client = AsyncIOMotorClient("mongodb://18.190.253.104:5505/")
        self.database = self.client["connecta"]
        self.service = self.database["service"]
        self.users = self.database["users"]
        self.tickets = self.database["tickets"]

    
    async def close(self):
        self.client.close()
    
    async def insert_user(self, user):
        pass
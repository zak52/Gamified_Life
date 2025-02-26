import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()  # Make sure this is called before accessing environment variables
MONGODB_URI = os.getenv("MONGODB_URI")
print("MONGODB_URI:", MONGODB_URI)  # Check the output in your terminal

client = AsyncIOMotorClient(MONGODB_URI)
db = client.get_default_database()  # This will use "mydatabase" from the URI
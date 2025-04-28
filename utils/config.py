import os
from dotenv import dotenv_values

current_env = os.getenv("ENV", "")
environment = "dev"
config = dotenv_values(f".env.{current_env}" if current_env else ".env") 
print(f".env.{current_env}" if current_env else ".env")

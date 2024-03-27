import os
from dotenv import load_dotenv

# Load environment variables from .env file
result = load_dotenv()

# Check if .env file was loaded successfully
if not result:
    print("Failed to load .env file")


class GetENV:

    def get_token(self):
        token = os.getenv("TOKEN")
        if token is None:
            raise ValueError("TOKEN environment variable is not set")
        return token

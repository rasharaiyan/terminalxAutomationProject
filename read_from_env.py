import os
from dotenv import load_dotenv

load_dotenv()

class GetENV:

    def get_token(self):
        token = os.getenv("TOKEN")
        if token is None:
            raise ValueError("TOKEN environment variable is not set")
        return token
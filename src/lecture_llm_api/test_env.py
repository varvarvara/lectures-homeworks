import os 

import dotenv
from dotenv import load_dotenv
load_dotenv()
dotenv.load_dotenv(dotenv.find_dotenv())

OPEN_BASE_URL: str = os.getenv("OPEN_BASE_URL", "HELLO")
OPEN_API_KEY: str = os.environ["OPEN_API_KEY"]
print(OPEN_BASE_URL)
# print(OPEN_API_KEY)
print(os.environ)
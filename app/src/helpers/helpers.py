from .shared import Shared
import os
from dotenv import load_dotenv

load_dotenv()

def get_style(style):
    file = open(Shared.STYLES_PATH / os.getenv(style), "r")
    content = file.read()
    file.close()
    return content
import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI DevOps Monitoring Dashboard")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
DEBUG = os.getenv("DEBUG", "True") == "True"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
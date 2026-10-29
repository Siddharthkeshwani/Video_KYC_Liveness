from dotenv import load_dotenv
import os

load_dotenv()

for name in ["ROBOFLOW_API_KEY", "HF_TOKEN","KAGGLE_USERNAME","KAGGLE_KEY"]:
    if os.getenv(name):
        print(name, "-> FOUND")
    else:
        print(name, "-> MISSING")
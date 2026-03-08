import requests
import os
import time

SERVER = "https://your-codespace-url/command"
TOKEN = "ULTRA_JARVIS_123"

print("Jarvis Laptop Agent Started")

while True:

    try:

        cmd = requests.get(
            SERVER,
            params={"token": TOKEN}
        ).text.strip()

        if cmd:

            print("Executing:", cmd)

            os.system(cmd)

    except:
        pass

    time.sleep(3)

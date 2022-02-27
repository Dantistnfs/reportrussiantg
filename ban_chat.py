import time
from telethon.sync import TelegramClient
from telethon.tl.functions.account import ReportPeerRequest
from telethon.tl.types import InputReportReasonViolence
import requests
import random
from tqdm import tqdm
import sqlite3


requests_limit = 100
requests_reset = 60*60*24 # 1 DAY
requests_done = 0
time_to_reset = time.time() + requests_reset


con = sqlite3.connect('db/status.db')
cursor = con.cursor()
cursor.execute(f"""CREATE TABLE IF NOT EXISTS reported (
    channel TEXT)""")
con.commit()

reasons = ["Ukraine", "Russian invasion", "War in Ukraine", "Russia started war", "Terrorism",
           "Російське вторгнення","Російське вторгнення в Україну"]
end_symbols = ["!",".","!!","!!!"]

api_id = 17298364
api_hash = '80727307a3ba5fbddb016dcb531afeef'
client = TelegramClient('tgautomate', api_id, api_hash)
client.start()


print("Bans go brrrrr")

while True:
    chat_id_to_report_list = requests.get("https://fuckrussianbots.xyz/static/latest_list.csv").text.split("\n")
    for channel in tqdm(chat_id_to_report_list):
        if channel and (not cursor.execute(f"""SELECT 1 FROM reported WHERE channel = '{channel}'""").fetchone()):
            if random.random() > 0.3: # Randomly report 70% of file
                if time.time() > time_to_reset: # Reset if already 24h passed from start
                    requests_done = 0
                    time_to_reset = time.time() + requests_reset
                if requests_done < requests_limit:
                    requests_done += 1
                    try:
                        response = client(ReportPeerRequest(channel, 
                                                            reason=InputReportReasonViolence(), 
                                                            message=f"{random.choice(reasons)}{random.choice(end_symbols)}"))
                        print(f"Reported {channel}")
                    except Exception as e:
                        print(f"Exception in sending ban to {channel}")
                        print(e)
                    sleep_until_next_report = 30+30*random.random() # from 1 minute to 10 minutes
                    print(f"Sleeping {sleep_until_next_report/60} minutes")
                    time.sleep(sleep_until_next_report)
                    cursor.execute(f"""INSERT INTO reported(channel) VALUES(?)""", (channel,))
                    con.commit()
                else:
                    time.sleep(time_to_reset - time.time()) # Sleep until reset rate
    print("Sleeping")
    time.sleep(60) # sleep minute before check


import os
import subprocess
import zipfile
import glob

from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, CreateNewSession, UseCurrentSession
import asyncio

file = os.environ['ACCOUNT_MEGA_LINK']

try:
    print("Trying to use megatools get")
    subprocess.run(["megadl", file])
except Exception as FileNotFoundError:
    print("Proably you are using newer version of megatools, using instead mega-get")
    subprocess.run(["mega-get", file])

downloaded_zip = glob.glob("*.zip")[0]
zip = zipfile.ZipFile(downloaded_zip)
zip.extractall('account')

tdata = glob.glob("account/*/tdata")[0]


async def main():
    
    # Load TDesktop client from tdata folder
    tdesk = TDesktop(tdata)

    # Using official iOS API with randomly generated device info
    # print(api) to see more
    api = API.TelegramDesktop.Generate(system="windows")
    api.system_version = "Windows 10"
    api.system_lang_code = "ru-RU"


    # Convert TDesktop session to telethon client
    # CreateNewSession flag will use the current existing session to
    # authorize the new client by `Login via QR code`.
    client = await tdesk.ToTelethon("bot.session", CreateNewSession, api)

    # Although Telegram Desktop doesn't let you authorize other
    # sessions via QR Code (or it doesn't have that feature),
    # it is still available across all platforms (APIs).

    # Connect and print all logged in devices
    await client.connect()

asyncio.run(main())


import configparser
import pandas as pd
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors import UserPrivacyRestrictedError, UserNotMutualContactError
import asyncio
import openpyxl

configParser = configparser.ConfigParser()
configParser.read("config.ini")

api_id = int(configParser["telegram"]["api_id"])
api_hash = configParser["telegram"]["api_hash"]
phone_number = configParser["telegram"]["phone"]
excel_file = "telegram_usernames.xlsx"
target_group = "https://t.me/+WkbWpk5GSDU4ZTA1"

df = pd.read_excel(excel_file)
usernames = df['usernames'].dropna().tolist()

for user in usernames:
    user = user.lstrip("@")

client = TelegramClient("Test session", api_id, api_hash)

async def main():
    await client.start(phone=phone_number)

    group = await client.get_entity(target_group)

    for username in usernames:
        try: 
            user = await client.get_entity(username)
            await client(InviteToChannelRequest(group,[user]))
            print(f"Sent invite {username} to {target_group}")

            await asyncio.sleep(3)
        except (UserNotMutualContactError, UserPrivacyRestrictedError) as e:
            print(f"Failed to invite {username}: {e}\n")
            print(f"Attemtping to send invite link..")
            
            try:
                await client.send_message(username, f"Hi! Please join the group {target_group}")
                print(f"sent invite to {username}")

                await asyncio.sleep(3)
            except Exception as e:
                print(f"erm, failed to send invite to {username}: {e}")
        except Exception as e:
            print(f"hey wtf happened man: {e}")
    
with client:
    client.loop.run_until_complete(main())



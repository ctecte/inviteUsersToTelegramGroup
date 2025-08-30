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
            result = await client(InviteToChannelRequest(group,[user]))

            # uncomment this to see who is being added
            # print(f"Adding {username} to group {target_group}...")
            
            # i have to click through 5 pages of redirect to find there is a property called missing_invitees WTF IS THIS SHIT
            # For future reference
            # https://tl.telethon.dev/constructors/messages/invited_users.html 
            if (result.missing_invitees):
                print(f"{username} has turned off 'add to group'. Trying to send invite link instead..")
                try:
                    await client.send_message(username, f"Hi! Please join the group {target_group}")
                    print(f"Invited {username}")

                    # await asyncio.sleep(3)
                except Exception as e:
                    print(f"erm, failed to send invite to {username}: {e}")
            else:
                print(f"{username} added successfully")
            await asyncio.sleep(3)
        # This doesnt work. The function literally doesnt even throw its own errors that it has listed in documentation
        # except (UserNotMutualContactError, UserPrivacyRestrictedError) as e:
        #     print(f"Failed to invite {username}: {e}\n")
        #     print(f"Attemtping to send invite link..")
            
        except Exception as e:
            print(f"hey wtf happened man: {e}")

    
with client:
    client.loop.run_until_complete(main())



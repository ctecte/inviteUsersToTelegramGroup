# Use instructions

THIS ONLY WORKS FOR SUPERGROUPS. Uses your own account to add people. Could result in your account being flagged for spam, so do not remove the await asyncio.sleep() calls
You must be admin to add people to group, otherwise, read the side note below.  

A 1 minute video on making a group into a supergroup:
https://www.youtube.com/watch?v=S1bQ3JF4ow0

<img width="602" height="549" alt="image" src="https://github.com/user-attachments/assets/1ae52a7b-67c6-4d51-8dd8-b62218f11bbd" />


## CREATE a file called config.ini, and paste this inside the same folder as bot.py
```
[telegram]
api_id=12345678
api_hash=27c95073aa855asdfasfasdfasddf
phone=+6581234567
```
Replace the content with your own details

### if you dont have your api id and hash
https://core.telegram.org/api/obtaining_api_id

<img width="850" height="251" alt="image" src="https://github.com/user-attachments/assets/99a9f21f-8036-4e6a-b1fd-db4c42486812" />

Go to the telegram website and get your api id and hash. Make sure to save it somewhere, if you lose it its gone for good

Your telegram password is also probably required

## In bot.py

### Adjust path to excel_sheet, and ensure column name with usernames is called "usernames"
```
excel_file = "your_excel.xlsx"
```
otherwise adjust the df[column_name] function 
```
usernames = df['<your_column_name>'].dropna().tolist()
```

If the usernames contain the @ symbol eg: @telegram_user,
uncomment this line 
```
usernames = [user.strip().lstrip("@") for user in usernames]
```

### Set the target_group variable to the group invite link
Note: you must be an admin to add people. The script will NOT work if you are not admin.
```
target_group = "https://t.me/+WkbWpkABCDEFG"
```

You can adjust this invite message if the user cannot be added to group
```
await client.send_message(username, f"Hi! Please join the group {target_group}")
```

# Recommended to run the bot in a virtual environment
Run commands one by one
#### Windows
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python bot.py


# type this to exit venv 
deactivate
```

#### Linux/Mac
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python bot.py

# type to exit venv
deactivate
```

#### Side note:
To get this to work as non admin
remove these 2 lines and fix the indentation accordingly
```
result = await client(InviteToChannelRequest(group,[user]))
if (result.missing_invitees):
```
This will send just the invite link to everybody and not attempt to add people to group






















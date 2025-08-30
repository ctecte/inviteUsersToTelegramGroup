# Use instructions

THIS ONLY WORKS FOR SUPERGROUPS
A 1 minute video on making a group into a supergroup

https://www.youtube.com/watch?v=S1bQ3JF4ow0

<img width="602" height="549" alt="image" src="https://github.com/user-attachments/assets/1ae52a7b-67c6-4d51-8dd8-b62218f11bbd" />


### create a file called config.ini, and replace this inside
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

### Add an excel sheet and ensure the column name with usernames is just called "usernames"
or adjust the pd.read function with the column name
```
usernames = df['<your column name>'].dropna().tolist()
```

### Adjust the excel_sheet variable as needed to the name of your .xlsx
```
excel_file = "your_excel.xlsx"
```

### Recommended to run the bot in a virtual environment

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python bot.py


# type this to exit venv 
deactivate
```






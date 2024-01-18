# P0: GroupMe Bot

## Setup

In order for the bot to run correctly, your `.env` file must have a USER_ID parameter that corresponds to your unique user id. For example it should include the line `USER_ID="[USER_ID]"`.  

The bot.py file already contains the line `USER_ID = os.getenv("USER_ID")` which will allow the script to run correctly as long as the user id is specififed in the `.env` file as shown above.

## Features

The GroupMe bot I have created is a copy bot. The bot echos everything you say except when you send a message saying "stop copying me" in which case the bot will apologize.

## How to Run

Run by entering `python3 bot.py` in the command line.

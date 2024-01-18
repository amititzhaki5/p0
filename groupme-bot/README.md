# P0: GroupMe Bot

## Setup

In order for the bot to run correctly, your `.env` file must have a USER_ID parameter that corresponds to your unique user id.  
In addition, your bot.py file must contain the line `USER_ID = os.getenv("USER_ID")` for the script to run correctly.

## Features

The GroupMe bot I have created is a copy bot. The bot echos everything you say except when you send a message saying "stop copying me" in which case the bot will apologize.

## How to Run

Run by entering `python3 bot.py` in the command line.

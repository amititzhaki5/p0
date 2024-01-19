# P0: GroupMe Bot

## Setup

In order for the bot to run correctly, your `.env` file must have a USER_ID parameter that corresponds to your unique user id. For example it should include the line `USER_ID="[USER_ID]"`.  

The bot.py file already contains the line `USER_ID = os.getenv("USER_ID")` which will allow the script to run correctly as long as the user id is specififed in the `.env` file as shown above.

## Features

The GroupMe bot I have created allows you to ask a question (your question must end in a question mark) and the bot will generate a response from Chat GPT. If the ChatGPT feature does not work in the virtual environment then you may need to run the command `pip install openai==0.28`.   The API key cannot be uploaded to GitHub or it will be deactivated, so I have sent it in a separate email to the TAs. Please put the API key at the top of the bot.py file where it says `openai.api_key = 'Enter API Key Here'`.
If you don't ask the bot a quesiton, it will just copy what you say. The bot echos everything you say except when you send a message saying "stop copying me" in which case the bot will apologize.

## How to Run

Run by entering `python3 bot.py` in the command line.

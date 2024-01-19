import requests
import time
import json
import os
from dotenv import load_dotenv
import pandas as pd
import openai
import time

openai.api_key = 'Enter API Key Here'

load_dotenv()

BOT_ID = os.getenv("BOT_ID")
GROUP_ID = os.getenv("GROUP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")
LAST_MESSAGE_ID = None


def send_message(text, attachments=None):
    """Send a message to the group using the bot."""
    post_url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": BOT_ID, "text": text, "attachments": attachments or []}
    response = requests.post(post_url, json=data)
    return response.status_code == 202


def get_group_messages(since_id=None):
    """Retrieve recent messages from the group."""
    params = {"token": ACCESS_TOKEN}
    if since_id:
        params["since_id"] = since_id

    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:
        # this shows how to use the .get() method to get specifically the messages but there is more you can do (hint: sample.json)
        return response.json().get("response", {}).get("messages", [])
    return []


def process_message(message):
    """Process and respond to a message."""
    global LAST_MESSAGE_ID
    text = message["text"].lower()

    sender_type = message["sender_type"]
    name = message["name"]
    user_id = message["user_id"]

    # i.e. responding to a specific message (note that this checks if "hello bot" is anywhere in the message, not just the beginning)
    if "good morning" in text and sender_type == "user":
        send_message("good morning, " + name) 
    elif "good night" in text and sender_type == "user":
        send_message("good night, " + name) 
    elif user_id == USER_ID:
        # If you ask question, the bot will provide a response from Chat GPT
        if text[-1] == "?":
            prompt = text
            response = get_ChatGPT_response(prompt=prompt)
            send_message("ChatGPT says: " + response)
        # If you tell the bot "stop copying me then it will apologize"
        elif "stop copying me" in text:
            send_message("Sorry!")
        else:
            # Else, the bot will just repeat what you say
            send_message(text)
    
    LAST_MESSAGE_ID = message["id"]

def get_ChatGPT_response(prompt,model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(model=model,messages=messages,temperature=0)
    return response.choices[0].message.content


def main():
    global LAST_MESSAGE_ID
    # this is an infinite loop that will try to read (potentially) new messages every 10 seconds, but you can change this to run only once or whatever you want
    while True:
        messages = get_group_messages(LAST_MESSAGE_ID)
        for message in reversed(messages):
            process_message(message)
        time.sleep(10)


if __name__ == "__main__":
    main()

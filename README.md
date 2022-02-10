## Rubber-Price-Telegram-Bot

![MIT License](https://img.shields.io/github/license/shine-jayakumar/Covid19-Exploratory-Analysis-With-SQL)

Rubber Price Bot is a Telegram bot that waits for the user's cue and replies with the latest rubber prices. Rubber prices are extracted from: http://rubberboard.org.in/public using ``` requests ``` and ``` BeautifulSoup ```

![Bot Image](https://github.com/shine-jayakumar/Rubber-Price-Telegram-Bot/blob/master/bot_screenshot.PNG)

**Table of Contents**
- [Why Did I?](#Why-Did-I "Why Did I?")
- [How Does It Work?](#How-Does-It-Work "How Does It Work?")
- [Requirements](#Requirements "Requirements")
- [Script Link](#Script-Link "Script Link")

## Why-Did-I
My father practices rubber tapping as part of his post-retirement hobby. Rubber prices vary daily. He needs to know the current price to make a profitable sale. 
Now, he isn't great at searching things on Google, so I made this bot so he could get the latest price just by sending a message through Telegram.

## How-Does-It-Work
Rubber Price Bot is a Telegram bot that is hosted on Heroku. The bot's webhook is configured with the bot's link. Whenever a user sends a message addressed to this bot, Telegram sends that message to the link configured in the bot's webhook.
Upon receiving a message, the bot extracts the current price from the website, and replies to the user using the user's unique chat id.

## Requirements
- Flask
- Flask-cors
- BeautifulSoup
    
    See the [requirements.txt](https://github.com/shine-jayakumar/Rubber-Price-Telegram-Bot/blob/master/requirements.txt)

## Script-Link
[Script Link](https://github.com/shine-jayakumar/Rubber-Price-Telegram-Bot/blob/master/bot.py)

## LICENSE
[LICENSE](https://github.com/shine-jayakumar/Rubber-Price-Telegram-Bot/blob/master/LICENSE)

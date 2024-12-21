# SJSU On-Campus Job Notifier

A Python utility that fetches on-campus job listings from multiple sources and sends notifications to a Telegram channel whenever a new position opens up. This project helps students and job seekers stay updated on available campus jobs in real-time.

## Supported Job Sources

| Source Name             | URL                             | Data Type         |
|-------------------------|-----------------------------------------|-------------------|
| **Associated Students** | [workforcenow.adp.com](https://workforcenow.adp.com/mascsr/default/mdf/recruitment/recruitment.html?cid=1f21e958-d199-4456-afb9-29fa26ef70be&amp;amp;amp;ccId=19000101_000001&amp;amp;amp;type=JS&amp;amp;amp;lang=en_US&selectedMenuKey=CareerCenter) | API |
| **Spartan Eats**        | [compassgroupcareers.com](https://www.compassgroupcareers.com/)      | HTML Web Scraping               |
| **Student Union**       | [applitrack.com](https://www.applitrack.com/sjsu/onlineapp/default.aspx) | JS Dump Scraping |


## Features

- Fetches job listings from 3 predefined sources (websites, APIs, or databases).
- Sends real-time notifications to a specified Telegram channel whenever a new job position is posted.
- Helps students stay informed about new opportunities with minimal manual effort.

## Prerequisites

Before using this script, ensure that you have the following:

- Python 3.7+ installed.
- `pip` package manager for installing Python libraries.
- A Telegram bot token (for interacting with the Telegram Bot API).
- A Telegram channel where the bot will send notifications.

## Installation

### Step 1: Install the required dependencies
```bash
pip install -r requirements.txt
```

This will install all the necessary libraries such as requests, python-telegram-bot, and others.

### Step 2: Set up the Telegram Bot
Open Telegram and search for BotFather.
Start a conversation with BotFather and use the /newbot command to create a new bot.
Once your bot is created, BotFather will give you an API token. Keep this token handy.

### Step 3: Set up the Configuration
Update your Database URL, Telegram bot API token and channel details to the secrets file.

### Step 4: Run the Script
Now, you can run the script to start fetching job listings and sending notifications:
```bash
python main.py
```
The script will periodically check for new job postings from the defined sources and notify the Telegram channel whenever new listings are found.

## Contributing
Feel free to fork this repository and submit pull requests with improvements or additional features. Whether it's fixing bugs, adding new sources, or improving the notification format, contributions are welcome!

## Author 
[**Abhi Jain**](https://www.linkedin.com/in/abhi-jain)

![ForTheBadge built-by-developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)
![ForTheBadge_made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)
![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)

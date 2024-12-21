from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

from constants.secrets import Secrets
from utils.utils import date_convert_iso, get_pst


def format_job_message(job):
    title = job.get('title', 'No Title')
    date = job.get('date', 'No Date')
    job_id = job.get('id', 'No ID')
    link = job.get('link', '#')

    message = (
        f"📢 **New Job Opening!** 📢\n\n"
        f"🏢 {title}\n"
        f"📅 {date_convert_iso(date)}\n"
        f"🆔 {job_id}\n\n"
        f"Don't miss this opportunity 🚀"
    )
    keyboard = [[InlineKeyboardButton(text="Apply Now", url=link)]]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    return message, reply_markup

async def send_notification(job_notification):
    bot = Bot(token=Secrets.tg_token)
    for job in job_notification:
        message, reply_markup = format_job_message(job)
        try:
            await bot.send_message(chat_id=Secrets.chat_id, text=message, reply_markup=reply_markup, parse_mode='Markdown')
            print("Message sent successfully!")
        except Exception as e:
            print(f"Error sending message: {e}")
    if not job_notification:
        message = (
            f"No new openings found\n\n"
            f"🕒 Last fetched at {get_pst()}\n"
        )
        await bot.send_message(chat_id=Secrets.chat_id, text=message)
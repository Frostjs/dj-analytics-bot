import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
import aiocron


# Get local env and set bot and dispatcher
load_dotenv()
group_id = int(os.environ.get('GROUP_CHAT_ID'))
bot = Bot(token=os.environ.get('BOT_TOKEN'))
dp = Dispatcher(bot)

async def send_task_collection_reminder():
    # Reminder about analytics tasks
    message_text = "Привет! Не забудьте внести в Kaiten задачи по аналитике сегодня до конца дня! 🚀"

    # Send the message
    await bot.send_message(group_id, message_text)

if __name__ == '__main__':
    # Schedule the task to run every Thursday at 10:00 (MSK Corrected to UTC)
    aiocron.crontab('0 7 * * 4', func=send_task_collection_reminder)

    # Start the bot
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, skip_updates=True)

import logging
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from datetime import datetime
from parser_script import schedule_parser
from rich import print
#log level6
logging.basicConfig(level=logging.INFO)

#bot init
Token = ""
bot = Bot(token=Token)
dp = Dispatcher(bot)

def schedule_for_today(day):
    now = datetime.now().isoweekday()
    week_day = day.get('name_' + str(now))
    week_lesson = day.get('lessons_' + str(now))
    description = week_day
    for i in week_lesson.keys():
        key = week_lesson.get(i).keys()
        day_content = week_lesson.get(i)
        for j in key:
            description += '\n' + day_content.get(j)
    return description


def schedule_for_week(day):
    description = ''
    for n in range(1, 6):
        week_day = day.get('name_' + str(n))
        week_lesson = day.get('lessons_' + str(n))
        description += str('\n\n' + week_day)
        for i in week_lesson.keys():
            key = week_lesson.get(i).keys()
            day_content = week_lesson.get(i)
            for j in key:
                description += '\n' + day_content.get(j)
    return description

@dp.message_handler(commands=['schedule_for_today'])
async def rozklad(message: types.Message):
    send = schedule_for_today(schedule_parser())
    await message.answer(send)


@dp.message_handler(commands=['schedule_for_week'])
async def rozklad_all(message: types.Message):
    send = schedule_for_week(schedule_parser())
    await message.answer(send)

# chat_and_group = {}
# @dp.message_handler(commands=['set_group'])
# async def set_group(message: types.Message):
#
#     group_id = message.chat.id
#     await message.answer(message.text)

#тестова функція для повідомлення про пару за 10 хв
async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)

        # await bot.send_message(649448453, 'description', disable_notification=True)


#run
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10))
    executor.start_polling(dp, skip_updates=True)
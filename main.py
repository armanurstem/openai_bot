import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

tg_bot_token = '6156696333:AAH9rZ8G9uxV86CNboSmqxw7AxXXt1Z9Y5U'

openai.api_key  = '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'

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.Message):
    text = message["text"]
    if text.startswith("GPT"):
        message.text = text.replace("GPT", "").strip()
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You:"]
    )
    await message.answer(response['choices'][0]['text'])

if __name__ == "__main__":
 executor.start_polling(dp, skip_updates=True)

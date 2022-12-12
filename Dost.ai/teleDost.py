import time

# import utils

from aiogram import Bot, Dispatcher, executor, types
import openai

BOT_TOKEN = "5886577739:AAEZxCXtCQ3j2IiwpRfJ_INwNLHyO4UgUiU"
OPENAI_TOKEN = "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"

openai.api_key = OPENAI_TOKEN
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def generateResponse(text):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"You: {text}\nFriend: ",
      temperature=0.5,
      max_tokens=60,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0,
      stop=["You:"]
    )
    return response['choices'][0]['text']

@dp.message_handler(content_types=types.ContentType.TEXT)
async def messageHandler(message: types.Message):
    await message.reply(generateResponse(message.text))

# @dp.message_handler(content_types=types.ContentType.VOICE)
# async def audioHandler(message: types.Voice):
#     bot.send_voice(message.as_json['from']['id'], utils.voiceResponse(utils.recognize(message.get_file())))

if __name__ == "__main__":
    executor.start_polling(dp)
    
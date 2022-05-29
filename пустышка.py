from aiogram import Bot, Dispatcher, types, executor
import users

token = "2019607929:AAE9ZfV4gZAup8jSAXKZ4MgLIj4dzMm91P0"

bot = Bot(token=token, parse_mode='html')
dp = Dispatcher(bot)

users.createDB()



@dp.message_handler(content_types=["photo"])
async def photo(message: types.Message):
    if message.from_user.id == message.chat.id:
        if message.from_user.id == 1527663110 or message.from_user.id == 795071883:
            pass
        else:
            cap = "@LoonaHellBossArt ♡\n<a href='t.me/LoonaArtsBot'>Наш бот - Our bot</a>\n\n#photo"
            foto = message.photo[-1].file_id
            c = 0
            for i in message.photo[-1].file_id:
                await bot.send_photo(1527663110, foto, caption=cap)
                c += 1
                print(i)
        await message.reply(f"{c} ля")
    else:
        await message.reply("Если вы хотите отправить арт на модерацию - пишите в личные сообщения с ботом.\n\n"
                            "If you want to send an art for moderation - write in private messages with the bot.")


if __name__ == '__main__':
    executor.start_polling(dp, fast=True, skip_updates=True)
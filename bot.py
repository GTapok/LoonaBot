from aiogram import Bot, Dispatcher, types, executor
import users

token = "5382560973:AAGUFXivpUC8MrH-v61_JBRmIrMdXa8swME"

bot = Bot(token=token, parse_mode='html')
dp = Dispatcher(bot)

users.createDB()

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    users.cur.execute(f"SELECT name FROM users where id = {message.from_user.id}")
    if users.cur.fetchone() == None:
        users.InsrtValue(message.from_user.first_name, message.from_user.id)
        await message.reply("Привет!\n"
                            "Этот бот сделан для канала @LoonaHellBossArt.\n"
                            "Пришли мне арт, и я отправлю его на модерацию.\n"
                            "Вы можете узнать количество ваших баллов контента нажав на /profile\n\n"
                            "Sup\n"
                            "This bot is made for the @LoonaHellBossArt channel.\n"
                            "Send me the art and I'll send it for moderation.\n"
                            "You can find out how many content points you have by clicking on /profile")
    else:
        await message.reply("Привет!\n"
                            "Этот бот сделан для канала @LoonaHellBossArt.\n"
                            "Пришли мне арт, и я отправлю его на модерацию.\n"
                            "Вы можете узнать количество ваших баллов контента нажав на /profile\n\n"
                            "Sup\n"
                            "This bot is made for the @LoonaHellBossArt channel.\n"
                            "Send me the art and I'll send it for moderation.\n"
                            "You can find out how many content points you have by clicking on /profile")


@dp.message_handler(content_types=["photo"])
async def photo(message: types.Message):
    if message.from_user.id == message.chat.id:
        if message.from_user.id == 1527663110 or message.from_user.id == 862085756:
            foto = message.photo[-1].file_id
            cap = "@LoonaHellBossArt ♡\n<a href='t.me/LoonaArtsBot'>Наш бот - Our bot</a>\n\n#photo"
            await bot.send_photo(-1001787348621, foto, caption=cap)
            await message.reply("Я отправил арт на канал.")
        else:
            foto = message.photo[-1].file_id
            cap = f"Фото от пользователя <a href='tg://openmessage?user_id={message.from_user.id}'>{message.from_user.first_name}</a>, @{message.from_user.username}"
            await bot.send_photo(1527663110, foto, caption=cap)
            await bot.send_photo(862085756, foto, caption=cap)
            users.UpVa("arts", 1, message.from_user.id)
            users.conn.commit()
            await message.reply("Фото было отправлено админам, ожидайте одобрения.\n\n"
                                "The photo has been sent to the admins, please wait for approval.")
    else:
        await message.reply("Если вы хотите отправить арт на модерацию - пишите в личные сообщения с ботом.\n\n"
                            "If you want to send an art for moderation - write in private messages with the bot.")

@dp.message_handler(content_types=["video"])
async def video(message: types.Message):
    if message.from_user.id == message.chat.id:
        if message.from_user.id == 1527663110 or message.from_user.id == 862085756:
            foto = message.video.file_id
            cap = "@LoonaHellBossArt ♡\n<a href='t.me/LoonaArtsBot'>Наш бот - Our bot</a>\n\n#video"
            await bot.send_video(-1001787348621, foto, caption=cap)
            await message.reply("Я отправил видео на канал.")
        else:
            foto = message.video.file_id
            cap = f"Видео от пользователя <a href='tg://openmessage?user_id={message.from_user.id}'>{message.from_user.first_name}</a>, @{message.from_user.username}"
            await bot.send_video(1527663110, foto, caption=cap)
            await bot.send_video(862085756, foto, caption=cap)
            users.UpVa("arts", 1, message.from_user.id)
            users.conn.commit()
            await message.reply("Видео было отправлено админам, ожидайте одобрения.\n\n"
                                "The video has been sent to the admins, please wait for approval.")
    else:
        await message.reply("Если вы хотите отправить видео на модерацию - пишите в личные сообщения с ботом.\n\n"
                            "If you want to send an video for moderation - write in private messages with the bot.")


@dp.message_handler(commands=["profile"])
async def profile(message: types.Message):
    if message.from_user.id == 1527663110 or message.from_user.id == 862085756:
        a = users.cur.execute(f"SELECT arts FROM users")
        koll = len(a)
        await message.reply(koll)

    else:
        for a in users.cur.execute(f"SELECT arts FROM users where id = {message.from_user.id}"):
            await message.reply(f"Content points: {a[0]}.\n"
                                f"Очки контента: {a[0]}")

if __name__ == '__main__':
    executor.start_polling(dp, fast=True, skip_updates=True)
from aiogram import Bot, Dispatcher, types, executor
import users

token = "5382560973:AAGUFXivpUC8MrH-v61_JBRmIrMdXa8swME"

bot = Bot(token=token, parse_mode='html')
dp = Dispatcher(bot)

users.createDB()

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Привет!\n"
                        "Этот бот сделан для канала @LoonaHellBossArt.\n"
                        "Пришли мне арт, и я отправлю его на модерацию.\n"
                        "\n"
                        "Sup\n"
                        "This bot is made for the @LoonaHellBossArt channel.\n"
                        "Send me the art and I'll send it for moderation.\n")

@dp.message_handler(content_types=["photo"])
async def photo(message: types.Message):
    if message.from_user.id == message.chat.id:
        if message.from_user.id == 1527663110 or message.from_user.id == 862085756 or message.from_user.id == 795071883:
            foto = message.photo[-1].file_id
            cap = "@LoonaHellBossArt ♡\n<a href='t.me/LoonaArtsBot'>Наш бот - Our bot</a>\n\n#photo"
            await bot.send_photo(-1001787348621, foto, caption=cap)
            await message.reply("Я отправил арт на канал.")
        else:
            foto = message.photo[-1].file_id
            cap = f"Фото от пользователя <a href='tg://openmessage?user_id={message.from_user.id}'>{message.from_user.first_name}</a>, @{message.from_user.username}"
            await bot.send_photo(1527663110, foto, caption=cap)
            await bot.send_photo(862085756, foto, caption=cap)
            await message.reply("Фото было отправлено админам, ожидайте одобрения.\n\n"
                                "The photo has been sent to the admins, please wait for approval.")
    else:
        await message.reply("Если вы хотите отправить арт на модерацию - пишите в личные сообщения с ботом.\n\n"
                            "If you want to send an art for moderation - write in private messages with the bot.")

@dp.message_handler(content_types=["video"])
async def video(message: types.Message):
    if message.from_user.id == message.chat.id:
        if message.from_user.id == 1527663110 or message.from_user.id == 862085756 or message.from_user.id == 795071883:
            foto = message.video.file_id
            cap = "@LoonaHellBossArt ♡\n<a href='t.me/LoonaArtsBot'>Наш бот - Our bot</a>\n\n#video"
            await bot.send_video(-1001787348621, foto, caption=cap)
            await message.reply("Я отправил видео на канал.")
        else:
            foto = message.video.file_id
            cap = f"Видео от пользователя <a href='tg://openmessage?user_id={message.from_user.id}'>{message.from_user.first_name}</a>, @{message.from_user.username}"
            await bot.send_video(1527663110, foto, caption=cap)
            await bot.send_video(862085756, foto, caption=cap)
            await message.reply("Видео было отправлено админам, ожидайте одобрения.\n\n"
                                "The video has been sent to the admins, please wait for approval.")
    else:
        await message.reply("Если вы хотите отправить видео на модерацию - пишите в личные сообщения с ботом.\n\n"
                            "If you want to send an video for moderation - write in private messages with the bot.")

@dp.message_handler(content_types=["animation"])
async def gif(message: types.Message):
    if message.from_user.id == message.chat.id:
        if message.from_user.id == 1527663110 or message.from_user.id == 862085756 or message.from_user.id == 795071883:
            gif = message.animation.file_id
            cap = "@LoonaHellBossArt ♡\n<a href='t.me/LoonaArtsBot'>Наш бот - Our bot</a>\n\n#gif"
            await bot.send_animation(-1001787348621, gif, caption=cap)
            await message.reply("Я отправил видео на канал.")
        else:
            gif = message.animation.file_id
            cap = f"Гиф от пользователя <a href='tg://openmessage?user_id={message.from_user.id}'>{message.from_user.first_name}</a>, @{message.from_user.username}"
            await bot.send_animation(1527663110, gif, caption=cap)
            await bot.send_animation(862085756, gif, caption=cap)
            await message.reply("Гиф было отправлено админам, ожидайте одобрения.\n\n"
                                "The gif has been sent to the admins, please wait for approval.")
    else:
        await message.reply("Если вы хотите отправить гиф на модерацию - пишите в личные сообщения с ботом.\n\n"
                            "If you want to send an gif for moderation - write in private messages with the bot.")

@dp.message_handler(content_types=["sticker"])
async def send_sticker(message: types.Message):
    if message.from_user.id == message.chat.id:
        if message.from_user.id == 1527663110 or message.from_user.id == 862085756 or message.from_user.id == 795071883:
            stick = message.sticker.file_id
            cap = "@LoonaHellBossArt ♡\n<a href='t.me/LoonaArtsBot'>Наш бот - Our bot</a>\n\n#sticker"
            a = await bot.send_sticker(-1001787348621, stick)
            await bot.send_message(-1001787348621, cap)
            await message.reply("Готово")
        else:
            st = message.sticker.file_id
            cap = f"Стикер от пользователя <a href='tg://openmessage?user_id={message.from_user.id}'>{message.from_user.first_name}</a>, @{message.from_user.username}"
            await bot.send_sticker(1527663110, st)
            await bot.send_sticker(862085756, st)
            await bot.send_message(862085756, cap)
            await bot.send_video(1527663110, cap)
            await message.reply("Стикер был отправлен админам, ожидайте одобрения.\n\n"
                                "The sticker has been sent to the admins, please wait for approval.")
    else:
        await message.reply("Если вы хотите отправить стикер на модерацию - пишите в личные сообщения с ботом.\n\n"
                            "If you want to send an sticker for moderation - write in private messages with the bot.")

@dp.message_handler(commands=["ok"])
async def ok(message: types.Message):
    if message.from_user.id == 1527663110 or message.from_user.id == 862085756 or message.from_user.id == 795071883:
        if message.reply_to_message.photo:
            try:
                document_id = message.reply_to_message.photo[0].file_id
                foto = await bot.get_file(document_id)
                cap = "@LoonaHellBossArt ♡\n<a href='t.me/LoonaArtsBot'>Наш бот - Our bot</a>\n\n#photo"
                await bot.send_photo(chat_id=-1001787348621, photo=foto.file_id, caption=cap)
                await message.reply("Готово")
            except Exception as e:
                await message.reply(f"В ответ на сообщение \n\n{e}")
        if message.reply_to_message.video:
            try:
                vid = message.reply_to_message.video.file_id
                cap = "@LoonaHellBossArt ♡\n<a href='t.me/LoonaArtsBot'>Наш бот - Our bot</a>\n\n#video"
                await bot.send_video(chat_id=-1001787348621, video=vid, caption=cap)
                await message.reply("Готово")
            except Exception as e:
                await message.reply(f"В ответ на сообщение\n\n{e}")

        if message.reply_to_message.animation:
            try:
                gif = message.reply_to_message.animation.file_id
                cap = "@LoonaHellBossArt ♡\n<a href='t.me/LoonaArtsBot'>Наш бот - Our bot</a>\n\n#gif"
                await bot.send_animation(chat_id=-1001787348621, animation=gif, caption=cap)
            except Exception as e:
                await message.reply(f"В ответ на сообщение\n\n{e}")
    else:
        pass


if __name__ == '__main__':
    executor.start_polling(dp, fast=True, skip_updates=True)
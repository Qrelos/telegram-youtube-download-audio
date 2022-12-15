import config
import telebot
from pytube import YouTube
import os

bot = telebot.TeleBot(config.telegram_token)

@bot.message_handler()
def add(audio):
    bot.register_next_step_handler(audio, add)
    if audio.text is None or audio.text.find('youtu') < 0:
        bot.send_message(audio.chat.id, 'Принимаются только ссылки на ютуб')
    else:
        yt = YouTube(audio.text)
        bot.send_message(audio.chat.id, yt.title)
        stream = yt.streams.get_by_itag(139)
        audioz = stream.download()
        with open(audioz, 'rb') as podkast:
            bot.send_audio(audio.chat.id, podkast)
        os.remove(audioz)


bot.polling(none_stop=True)
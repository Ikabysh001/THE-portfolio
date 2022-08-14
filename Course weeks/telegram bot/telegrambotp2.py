from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

import random,requests
from bs4 import BeautifulSoup
import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS
import os
        


def get_weather(city_name):
    api_key = "87a478799946582566e1eebe9804d7ea"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = base_url = base_url+ "appid="  + api_key + "&q=" +city_name
    response = requests.get(complete_url)
    x=response.json()
    visibility = x['visibility']
    weather = x['weather'][0]['description']
    timezone = x['timezone']
    temp = x["main"]["temp"]-273
    humidity = x["main"]["humidity"]
    w = "weather:"+str(weather)+"\n"+"visibility:"+str(visibility)+"m"+"\n"+"timezone:"+str(timezone)+"hours"+"\n"+"temp:"+str(int(temp))+"°"+"\n"+"humidity:"+str(humidity)+"%"+"\n"
    return w


api_key = "5592873776:AAGeLg53cvjYcEbYUkiOz16rXsb5h6kFPGc"
updater = Updater(api_key,use_context=True)
link = ["https://vm.tiktok.com/ZMNUF73F5/?k=1","https://vm.tiktok.com/ZMNUFGLQm/?k=1","https://vm.tiktok.com/ZMNUYjG3K/?k=1",
        "https://vm.tiktok.com/ZMNUFTmf3/?k=1","https://vm.tiktok.com/ZMNUYNpho/?k=1","https://vm.tiktok.com/ZMNUYe3MS/?k=1",
        "https://vm.tiktok.com/ZMNUYkfdB/?k=1","https://vm.tiktok.com/ZMNUYfbYv/?k=1","https://vm.tiktok.com/ZMNUY4H3L/?k=1",
       "https://vm.tiktok.com/ZMNUY4H3L/?k=1","https://vm.tiktok.com/ZMNUYAcRf/?k=1"]



memes = ["2HowtomakeamemeCanva.webp","images-3.jpg","74674380.webp","images-4.jpg","74674381.webp","images-5.jpg",
"74674393.webp","images-6.jpg","EvtBUYoXcAcCLeb.jpg","images-7.jpg","MEME-TIMELINE-AND-EVOLUTION.png","images-8.jpg"]



def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to my bot, use /help to find out what I can do")

def introduce(update: Update, context: CallbackContext):
    update.message.reply_text("Hello my name is R2D2")

def tiktok(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(link))

def help(update: Update, context:CallbackContext):
    update.message.reply_text("use:\n\
/introduce to read about me, also you can use: \
\n /tiktok to watch a short video which is supposedly funny ontop of that us \n \
futhermore, with a little web scraping i \
learned to get \n/weather (and the na,e of the  town or city after \
it in the same line) \n /btc is to see the current price of bitcoin \
/n /trend this is to post a video whic is trending but only use once \
 /n i mean it, if you do this bot wil get banned for spamming by tiktok")

def meme (update: Update,context:CallbackContext):
    image_folder=r"images"
    update.message.reply_photo(photo=open(image_folder+random.choice(memes), 'rb'))
    

def weather(update: Update, context:CallbackContext):
        reply = update.message.text
        city = reply[9:]
        print(city)
        w = get_weather(city)
        update.message.reply_text(w)

def btc(update: Update, context:CallbackContext):
    URL = "https://www.coingecko.com/en/coins/bitcoin"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    p = soup.find_all("div", class_="tw-text-4xl tw-font-bold tw-my-2 tw-flex tw-items-center")
    data = []
    for i in p:
        data.append(i.text.strip())
    update.message.reply_text(str(data[0])[0:7])

def unkown_text(update: Update, context:CallbackContext):
     update.message.reply_text(
         "Sorry I can't recognize , youyou said '%s'"% update.message.text)

def unkown (update: Update, context:CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command"  % update.message.text)

def trend(update: Update, context:CallbackContext):
    URL = "https://www.tiktok.com/discover/top-trending?lang=en"
    index = random.randint(1,9)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,  "html.parser")
    df = soup.find("div",{'data-video-index' :index})
    df = str(df)
    ls = df.split(" ")
    link = "www.tiktok.com"+ls[7][6:-6]
    update.message.reply_text(link)

def convert_ogg2wav(ofn):
    wfn = ofn.replace('.ogg','.wav')
    x = AudioSegment.from_file(ofn)
    x.export(wfn, format='wav')


def get_voice (update: Update, context: CallbackContext):
    new_file = context.bot.get_file(update. message. voice. file_id)
    new_file.download(f"voice_note.ogg")
    convert_ogg2wav("voice_note.ogg")

    recogniser = sr. Recognizer()
    sound = sr. AudioFile('voice_note.wav')
    with sound as source:
        audio = recogniser .record(source)
    text = recogniser.recognize_google(audio)
    update. message.reply_text ("in the voice message you have said: \n"+text)

def convert_to_voice(text):
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save("ivan.wav")
    os.system("mpg321 ivan.wav")

    reply = update.message.text
    convert_to_voice(reply[15:])
    update.message.reply_voice(open("ivan.wav", 'rb'))

def text_to_voice(update: Update, context:CallbackContext):
    reply = Update.message.text
    convert_to_voice(reply[15:])
    update.message.reply_voice(open("ivan.wav", 'rb'))


updater.dispatcher.add_handler(CommandHandler('text_to_voice', text_to_voice))
updater.dispatcher.add_handler(MessageHandler(Filters.voice , get_voice))
updater.dispatcher.add_handler(MessageHandler(Filters.voice , get_voice))
updater.dispatcher.add_handler(CommandHandler('trend', trend))
updater.dispatcher.add_handler(CommandHandler('btc', btc))
updater.dispatcher.add_handler(CommandHandler('weather', weather))
updater.dispatcher.add_handler(CommandHandler('start', start))   
updater.dispatcher.add_handler(CommandHandler('introduce', introduce))
updater.dispatcher.add_handler(CommandHandler('tiktok', tiktok))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('meme', meme))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unkown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unkown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unkown_text))

updater.start_polling()

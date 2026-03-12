import telebot
import asyncio
import logging
import subprocess

subprocess.run("pip install funpayace", shell=True)

from funpayace import FunpayAce, FunpayConfig

bot = telebot.TeleBot('8675951751:AAGBwLmpX1Yb-QCbCwSXD7gqD9RrAkzQKY0')

GOLDEN_KEY = "6o1mrmxqbh2spjoct0z0y6fe5rvxcsgu"
#golden_key = "0iep8rib5nc1sy6y71ojzaje5xfdjrq0"

balance=''

@bot.message_handler(commands=['start'])
def start(message):
    for x in range(1,6):
        bot.reply_to(message, 'Иди нахуй')

@bot.message_handler(commands=['art'])
def start(message):
    bot.reply_to(message, 'Команда')

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.reply_to(message, 'Я пидорас')

@bot.message_handler(commands=['infa'])
def infa(message):
    text=str(message)
    with open("text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("text.txt","rb") as file:
        bot.send_document(message.chat.id, file)

@bot.message_handler(commands=['namaz'])
def namaz(message):
    bot.send_message(message.chat.id, 'Cубханакаллахумма уа бихамдик,')
    bot.send_message(message.chat.id, 'уа табарака смук,')
    bot.send_message(message.chat.id, 'уа та’аля джаддук,')
    bot.send_message(message.chat.id, 'уа ля иляха гойрук.')
    bot.send_message(message.chat.id, 'Аʼузу билляхи минаш-шайтанир-раджим,')
    bot.send_message(message.chat.id, 'бисмилляхи-р-Рахмани-р-Рахим.')


@bot.message_handler(commands=['infafp'])
def infa(message):
    global balance
    logging.basicConfig(level=logging.INFO)


    async def main():
        #client1 = FunpayAce(golden_key=golden_key, config=FunpayConfig())
        client = FunpayAce(golden_key=GOLDEN_KEY, config=FunpayConfig())
        async with client:


            balance = str(await client.get_balance())[8:][:8]
            #balance1 = str(await client1.get_balance())[8:][:6]
            bot.send_message(message.chat.id, f'Баланс Libro11: {balance} рублей')
            await client.cancel_background_tasks()
#\nБаланс FIiz0r: {balance1} рублей
    if __name__ == "__main__":
        asyncio.run(main())




bot.infinity_polling()

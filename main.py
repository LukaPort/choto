import telebot
import asyncio
import logging
import subprocess

subprocess.run("pip install funpayace", shell=True)

from funpayace import FunpayAce, FunpayConfig

bot = telebot.TeleBot('8675951751:AAGBwLmpX1Yb-QCbCwSXD7gqD9RrAkzQKY0')

GOLDEN_KEY = "6o1mrmxqbh2spjoct0z0y6fe5rvxcsgu"
golden_key = "ap90fho0m2xa299htgg0s36460t82wrg"

balance=''


@bot.message_handler(commands=['infafp'])
def infafp(message):
    if message.from_user.username == D0X_EXPERT or message.from_user.username == QC11L:
        global balance
        logging.basicConfig(level=logging.INFO)
    
    
        async def main():
            client1 = FunpayAce(golden_key=golden_key, config=FunpayConfig())
            client = FunpayAce(golden_key=GOLDEN_KEY, config=FunpayConfig())
            async with client:
    
    
                balance = str(await client.get_balance())[8:][:8]
                balance1 = str(await client1.get_balance())[8:][:6]
                bot.send_message(message.chat.id, f'Баланс Libro11: {balance} рублей\nБаланс FIiz0r: {balance1} рублей')
                await client.cancel_background_tasks()
                
        if __name__ == "__main__":
            asyncio.run(main())
    else:
        bot.send_message(message.chat.if, 'У вас нет прав использовать данный бот')



bot.infinity_polling()

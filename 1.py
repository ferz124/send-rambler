import telegram
import time

# укажите токен вашего бота в переменной bot_token
bot_token = 'YOUR_BOT_TOKEN_HERE'

# создайте объект bot, используя указанный токен
bot = telegram.Bot(token=bot_token)

# создайте бесконечный цикл, который будет отправлять сообщение "Мне скучно" каждую минуту
while True:
    bot.send_message(chat_id='CHAT_ID_HERE', text='Мне скучно')
    time.sleep(60)  # задержка в 60 секунд

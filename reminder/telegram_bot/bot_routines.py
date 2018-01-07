

import logging
import telegram

# import mwt

logging.basicConfig(filename='telegram_bot2.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)

TOKEN = '345369460:AAGgeEcjoDtS2YCk9f8_N03rBUxjItk_vco'  # Astro-Bot
# TOKEN = '413894645:AAF_c_2tMqSS6MROVMtBtiEuaT0vYTwP31Q'  # FireFly-Notifier
# TOKEN = '540694160:AAFo4J6jRabVrJOrCJJBm8-NXTMHEGVhu3E'  # Ginn-Bot


def astro_bot_send_message(text):

    bot = telegram.Bot(token=TOKEN)
    print(bot.get_me())

    bot.send_message(chat_id=442763659, text=text)


# astro_bot_send_message('asfklafs')




# from functools import wraps
#
# LIST_OF_ADMINS = [12345678, 87654321]
#
# def restricted(func):
#     @wraps(func)
#     def wrapped(bot, update, *args, **kwargs):
#         user_id = update.effective_user.id
#         if user_id not in LIST_OF_ADMINS:
#             print("Unauthorized access denied for {}.".format(user_id))
#             return
#         return func(bot, update, *args, **kwargs)
#     return wrapped

#
# @mwt.MWT(timeout=60*60)
# def get_admin_ids(bot, chat_id):
#     """Returns a list of admin IDs for a given chat. Results are cached for 1 hour."""
#     return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]
#


# updates = bot.get_updates()
# print([u.message.text for u in updates])
#
# chat_id = bot.get_updates()[-1].message.chat_id
# print("chat_id=", chat_id)
#
# bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
# logging.info("I'm sorry Dave I'm afraid I can't do that.")


# {'id': 442763659, 'first_name': 'Serhii', 'is_bot': False, 'last_name': 'Surmylo', 'language_code': 'ru'}




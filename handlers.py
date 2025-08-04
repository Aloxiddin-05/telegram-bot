from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        f'Assalomu alaykum  {user.full_name}!.\n\n'
    
    )


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Qanday Yordam Kerak'
    )


def stop(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Botdan foydalanganiz uchun rahmat!'
    )

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

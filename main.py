from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import TOKEN

from handlers import start, help, echo, stop


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # command handler
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('stop', stop))

    # message handler
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

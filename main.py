from telegram.ext import MessageHandler, Filters, Updater
from telegram.ext import CommandHandler

from wiki import search_wiki


token = 'token'


def echo(update, conext):
    txt = update.message.text

    if txt.lower() in ['привет', 'как дела', 'txt']:
        txt = 'И тебе привет ххх'

    update.message.reply_text(txt)


def start(update, conext):
    update.message.reply_text('Я устал\nДа-да-да')


def help(update, conext):
    update.message.reply_text('А Я устал\nНет-Нет-Нет')


def wiki(update, context):
    print(context.args)
    word = "".join(context.args)
    if word:
        update.message.reply_text("Идёт поиск...")
        summary, url = search_wiki(word)
        update.message.reply_text(summary+url)
    else:
        update.message.reply_text("Необходимо ввести запрос")


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    print('Бот запущен.../')

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('wiki', wiki))

    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
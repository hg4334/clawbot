from telegram.ext import Updater, CommandHandler

BOT_TOKEN = "7993689388:AAH8KiF0BVWM_gfC1c0VvuGh_EMHxhg9aoc"

def start(update, context):
    update.message.reply_text(
        "🤖 Bot is alive and running on Railway!"
    )

def main():
    print("🚀 Starting ClawBot...")

    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

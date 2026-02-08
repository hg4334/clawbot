import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("7993689388:AAH8Kif0BVVM_gfC1cOVvuGh_EMHxhg9aoc")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment variables")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 ClawBot is alive!\n\nI will help you find tools, offers and opportunities."
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ ClawBot started. Waiting for messages...")
    app.run_polling()

if __name__ == "__main__":
    main()

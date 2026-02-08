import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 BOT TOKEN
# Railway: liec Variables → BOT_TOKEN
# Local: ja gribi, vari ielikt tieši te (skat. Variant 2)
BOT_TOKEN = os.getenv("7993689388:AAH8Kif0BVVM_gfC1cOVvuGh_EMHxhg9aoc")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is running!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()



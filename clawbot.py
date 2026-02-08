import os
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# Read token from environment
BOT_TOKEN = os.getenv("7993689388:AAH8Kif0BVVM_gfC1cOVvuGh_EMHxhg9aoc")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing! Set it in Railway Variables.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot is alive and running on Railway!")

async def main():
    print("🚀 Starting ClawBot...")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())




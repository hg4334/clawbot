import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# =========================
# 🔑 TELEGRAM BOT TOKEN
# =========================
BOT_TOKEN = "7993689388:AAH8KiF0BVWM_gfC1c0VvuGh_EMHxhg9aoc"
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot is alive and running on Railway!"
    )

async def main():
    print("🚀 Starting ClawBot...")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())



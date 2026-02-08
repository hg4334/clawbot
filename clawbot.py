import os
import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ======================================================
# 🔐 BOT TOKEN LOADING
#
# ❗ IMPORTANT:
# You DO NOT paste your bot token in this file.
#
# 👉 The token MUST be added in Railway:
# Railway → Service → Variables → Add:
#
#   KEY:   BOT_TOKEN
#   VALUE: 7993689388:AAH8Kif0BVVM_gfC1cOVvuGh_EMHxhg9aoc
#
# ======================================================

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN is not set!")
    print("➡️  Go to Railway → Service → Variables and add BOT_TOKEN")
    sys.exit(1)


# ======================================================
# 🤖 TELEGRAM COMMANDS
# ======================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 ClawBot is LIVE!\n\n"
        "Running 24/7 on Railway 🚄\n"
        "More features coming soon 🔥"
    )


# ======================================================
# 🚀 MAIN APP
# ======================================================

def main():
    print("🚀 Starting ClawBot...")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot started successfully.")
    app.run_polling()


if __name__ == "__main__":
    main()

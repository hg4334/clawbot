import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ================= CONFIG =================
BOT_TOKEN = os.getenv("7993689388:AAH8Kif0BVVM_gfC1cOVvuGh_EMHxhg9aoc")

# MAIN AFFILIATE (tu vari mainīt vēlāk)
LINK_SYSTEME = "https://systeme.io/?sa=sa0262839535dec70a2e6c328b5ccefc736f958e40"

# ================= TEXTS =================
WELCOME_TEXT = (
    "🤖 Welcome.\n\n"
    "I help people find real ways to earn and learn online.\n"
    "No hype. No scams.\n\n"
    "What country are you from?"
)

ASK_TIME = (
    "How much time can you invest per day?\n"
    "1️⃣ Less than 1 hour\n"
    "2️⃣ 1–3 hours\n"
    "3️⃣ 3+ hours"
)

ASK_BUDGET = (
    "Do you have any budget to start?\n"
    "1️⃣ No budget\n"
    "2️⃣ Around €50\n"
    "3️⃣ €100+"
)

TASK_TEXT = (
    "📌 First small task:\n\n"
    "Spend 20–30 minutes understanding how affiliate or referral links work.\n\n"
    "When ready, type:\n"
    "• `done` – if finished\n"
    "• `tools` – to see useful platforms"
)

TOOLS_TEXT = (
    "Here is a tool many beginners use for structure:\n\n"
    "• organizing links\n"
    "• simple pages\n"
    "• basic follow-up\n\n"
    "You can explore it for free:\n"
    f"👉 {LINK_SYSTEME}"
)

LISTEN_TEXT = (
    "I’m listening.\n\n"
    "You can ask about:\n"
    "• earning online\n"
    "• referral programs\n"
    "• next steps"
)

# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    context.user_data["step"] = "country"
    await update.message.reply_text(WELCOME_TEXT)

# ================= MAIN HANDLER =================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    step = context.user_data.get("step")
    text = update.message.text.strip().lower()

    if step == "country":
        context.user_data["country"] = text
        context.user_data["step"] = "time"
        await update.message.reply_text(ASK_TIME)

    elif step == "time":
        context.user_data["time"] = text
        context.user_data["step"] = "budget"
        await update.message.reply_text(ASK_BUDGET)

    elif step == "budget":
        context.user_data["budget"] = text
        context.user_data["step"] = "task"
        await update.message.reply_text(TASK_TEXT)

    elif step == "task":
        if text == "tools":
            await update.message.reply_text(TOOLS_TEXT)
        elif text == "done":
            await update.message.reply_text(
                "Good.\n\n"
                "Consistency matters more than speed.\n\n"
                "If you want, type `tools` or ask a question."
            )
        else:
            await update.message.reply_text(LISTEN_TEXT)

    else:
        await update.message.reply_text(LISTEN_TEXT)

# ================= RUN =================
def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN not set in environment variables")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running 24/7...")
    app.run_polling()

if __name__ == "__main__":
    main()
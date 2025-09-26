from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import os

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
HEROKU_APP_NAME = "boiling-savannah-69748"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am CvvApiBot. Use /download <URL> to process."
    )

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Please provide a URL.")
        return

    url = context.args[0]
    api_url = f"https://{HEROKU_APP_NAME}.herokuapp.com/download?url={url}"
    
    try:
        resp = requests.get(api_url, timeout=10)
        # Debug: print response content
        print("API response:", resp.text)
        data = resp.json()  # JSON response

        # Agar JSON empty ho ya error ho
        if not data:
            await update.message.reply_text("❌ Empty response from API.")
            return

        await update.message.reply_text(data.get("message", "No message received"))
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

# Telegram bot setup
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("download", download))

app.run_polling()

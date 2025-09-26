from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import os

# Bot token environment variable se lein
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Heroku app name
HEROKU_APP_NAME = "boiling-savannah-69748"  # <-- yahan apna Heroku app name dalen

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am CvvApiBot. Use /download <URL> to process."
    )

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Please provide a URL.")
        return
    url = context.args[0]
    try:
        # Backend API call
        api_url = f"https://{HEROKU_APP_NAME}.herokuapp.com/download?url={url}"
        resp = requests.get(api_url)
        data = resp.json()  # JSON response
        await update.message.reply_text(data.get("message", "No message received"))
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

# Telegram bot setup
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("download", download))

app.run_polling()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

BOT_TOKEN = "8454018672:AAEBu9S-bOU_dARB7O7FrT7eezJYKJBwL5g"  # यहाँ अपना बॉट टोकन डालें

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am CvvApiBot. Use /download <URL> to process.")

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Please provide a URL.")
        return
    url = context.args[0]
    # Call your own API
    try:
        resp = requests.get(f"https://YOUR_HEROKU_APP_NAME.herokuapp.com/download?url={url}")
        data = resp.json()
        await update.message.reply_text(data.get("message", "No message received"))
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("download", download))

app.run_polling()

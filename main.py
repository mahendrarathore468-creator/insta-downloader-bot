from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8906344428:AAGSdHseDYf4WcXWE8LJGnQW_ALeT6_hY60"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "instagram.com" in text:
        await update.message.reply_text("Instagram link receive ho gaya.")
    else:
        await update.message.reply_text("Instagram link bhejo.")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()

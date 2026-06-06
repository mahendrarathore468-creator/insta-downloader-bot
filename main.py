from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8906344428:AAGSdHseDYf4WcXWE8LJGnQW_ALeT6_hY60"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "instagram.com" in text:
        await update.message.reply_text("Instagram link receive ho gaya.")
    else:
        await update.message.reply_text("Instagram link bhejo.")

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, handle))

if __name__ == "__main__":
    import asyncio

async def main():
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)

asyncio.run(main())

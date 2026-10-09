import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

VIDEOS = {
    "ilya": "BAACAgEAAxkBAAMWaslVF4Y3KZPyqHga32rRJs0PENQAAn4KAAJxo0hGDLoXzT9oWaE9BA",
    "dima": "BAACAgEAAxkBAAMYaslVW9_xReLAI8dj3q4XMpzlkjkAAn8KAAJxo0hGdc_5Ui7G4ck9BA",
}

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if ctx.args:
        key = ctx.args[0].lower()
        if key in VIDEOS:
            await update.message.reply_video(
                VIDEOS[key],
                caption=f"🎉 Поздравление от {key.capitalize()}!"
            )
            return
    await update.message.reply_text(
        "Привет, Гоша 💜\n\nНажми на карточку на сайте, чтобы получить видео!"
    )

async def dima(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_video(VIDEOS["dima"])

async def ilya(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_video(VIDEOS["ilya"])

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("dima", dima))
app.add_handler(CommandHandler("ilya", ilya))

print("Бот запущен, жду сообщения...")
app.run_polling()

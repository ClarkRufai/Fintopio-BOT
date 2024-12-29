from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7859498222:AAFURF4EtkX4DDSvvei1KBWyr7PQFpHs1wA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! Welcome to the bot.")

def main():
    app = Application.builder().token(TOKEN).build()

    # Add command handler
    app.add_handler(CommandHandler("start", start))

    # Run the bot
    app.run_polling()

if __name__ == "__main__":
    main()

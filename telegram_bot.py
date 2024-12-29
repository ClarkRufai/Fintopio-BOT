import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the start command handler
def start(update, context):
    update.message.reply_text("Hello! I'm your bot. How can I assist you today?")

# Define the echo function
def echo(update, context):
    update.message.reply_text(update.message.text)

# Define the error handler
def error(update, context):
    logger.warning(f'Update "{update}" caused error "{context.error}"')

# Main function to start the bot
def main():
    # Load the bot token from environment variables
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        raise ValueError("No TELEGRAM_BOT_TOKEN environment variable set.")

    # Initialize the updater and dispatcher
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))

    # Add message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Log all errors
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

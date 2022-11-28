from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open("logs.csv", "a") as file:
        file.write(f"{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text} \n")
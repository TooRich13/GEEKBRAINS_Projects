from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from spy import *
import phbook

book = phbook.Phonebook()

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()

    if "j" in items[1]:
        x = complex(items[1])
    else:
        x = float(items[1])

    if "j" in items[2]:
        y = complex(items[2])
    else:
        y = float(items[2])

    await update.message.reply_text(f'{x}+{y} = {x+y}')
    
    
async def dif_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()

    if "j" in items[1]:
        x = complex(items[1])
    else:
        x = float(items[1])

    if "j" in items[2]:
        y = complex(items[2])
    else:
        y = float(items[2])

    await update.message.reply_text(f'{x}-{y} = {x-y}')
    
    
async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()

    if "j" in items[1]:
        x = complex(items[1])
    else:
        x = float(items[1])

    if "j" in items[2]:
        y = complex(items[2])
    else:
        y = float(items[2])

    await update.message.reply_text(f'{x}*{y} = {x*y}')
    
    
async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()

    if "j" in items[1]:
        x = complex(items[1])
    else:
        x = float(items[1])

    if "j" in items[2]:
        y = complex(items[2])
    else:
        y = float(items[2])

    await update.message.reply_text(f'{x}/{y} = {x/y}')
    
    
async def print_phbook(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass
async def add_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass
async def del_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass

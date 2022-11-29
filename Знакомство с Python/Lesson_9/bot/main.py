from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot_commands import *
from spy import *





app = ApplicationBuilder().token("5646990274:AAFLe6ff6nMqrtEmxq5lTk30Ic4nHS6m_3c").build()


app.add_handler(CommandHandler("hello", hello))


app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("dif", dif_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("div", div_command))

app.add_handler(CommandHandler("ph_add", add_contact))
app.add_handler(CommandHandler("ph_del",del_contact))
app.add_handler(CommandHandler("ph_print", print_phbook))




app.run_polling()
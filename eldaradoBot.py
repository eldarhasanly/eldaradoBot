import sqlite3
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Function to fetch a random fact from the database
def get_random_fact() :
    conn = sqlite3.connect('facts.db')
    cursor = conn.cursor()

    cursor.execute("SELECT fact FROM facts ORDER BY RANDOM() LIMIT 1")
    fakt = cursor.fetchone()[0]

    conn.close()
    return fakt


# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) : 
    welcome_message = "Eldarado bota xoş gəlmisiniz! Hal-hazırda bazada olan 1000-dən artıq faktdan təsadüfi bir fakt öyrənmək üçün /fakt əmrini daxil edin. © 2024. Eldar Həsənli"
    await update.message.reply_text(welcome_message)

# Function to handle the /fakt command
async def fakt(update: Update, context) :
    fakt = get_random_fact()
    await update.message.reply_text(fakt)

# Main function to run the bot
def main() : 
    TOKEN = '8071279323:AAFvq7-jZFWzS67_ShqqLV3p7kBdv2hPukY'

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("fakt", fakt))
    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == '__main__' :
    main()
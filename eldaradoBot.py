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
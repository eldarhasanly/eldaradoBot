import sqlite3
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

def get_random_fact() :
    conn = sqlite3.connect('facts.db')
    cursor = conn.cursor()

    cursor.execute("SELECT fact FROM facts ORDER BY RANDOM() LIMIT 1")
    fakt = cursor.fetchone()[0]

    conn.close()
    return fakt


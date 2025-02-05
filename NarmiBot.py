from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters
import random
import json
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the start command
async def start(update: Update, context: CallbackContext):
    """Handles the /start command."""
    await update.message.reply_text("Hello! I'm NarmiBot. How can I assist you today? 😊")
    log_interaction(update.message.text, "Hello! I'm NarmiBot. How can I assist you today? 😊")

# Define the help command
async def help_command(update: Update, context: CallbackContext):
    """Handles the /help command."""
    help_text = """
Here are the commands you can try:

/start - Start the bot
/help - Show this help message
/info - Get information about this bot
/joke - Get a random joke
/quote - Get an inspirational quote
/calc <expression> - Calculate a math expression (e.g., /calc 2+2*3)
/mute - Mute a user in a group
/unmute - Unmute a user in a group
/kick - Kick a naughty user from the group
/ban - Ban a user from the group
/hello - Greet the user in a more personal way
/imran - know more about the developer
"""
    await update.message.reply_text(help_text)
    log_interaction(update.message.text, help_text)

# Define the info command
async def info_command(update: Update, context: CallbackContext):
    """Handles the /info command."""
    info_text = """
I am NarmiBot, a simple Telegram bot built by Imran Shiundu.
I can help with commands like jokes, quotes, and group management!
Try typing /help to see all available commands!
"""
    await update.message.reply_text(info_text)
    log_interaction(update.message.text, info_text)

# Define the joke command
async def joke_command(update: Update, context: CallbackContext):
    """Handles the /joke command."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
    ]
    joke = random.choice(jokes)
    await update.message.reply_text(joke)
    log_interaction(update.message.text, joke)

# Define the quote command
async def quote_command(update: Update, context: CallbackContext):
    """Handles the /quote command."""
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
        "Do what you can, with what you have, where you are. – Theodore Roosevelt",
        "Believe you can and you're halfway there. – Theodore Roosevelt",
    ]
    quote = random.choice(quotes)
    await update.message.reply_text(quote)
    log_interaction(update.message.text, quote)

# Define the calculator command
async def calc_command(update: Update, context: CallbackContext):
    """Handles the /calc command."""
    try:
        expression = " ".join(context.args)
        if not expression:
            await update.message.reply_text("Please provide a math expression. Example: /calc 2+2*3")
            return

        result = eval(expression)
        await update.message.reply_text(f"Result: {result}")
        log_interaction(update.message.text, f"Result: {result}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}. Please provide a valid math expression.")
        log_interaction(update.message.text, f"Error: {e}. Please provide a valid math expression.")

# Define the mute command for groups
async def mute_command(update: Update, context: CallbackContext):
    """Mute a user in the group."""
    if update.message.chat.type != 'private':
        if context.args:
            try:
                user_id = int(context.args[0])  # user ID should be provided after the command
                await context.bot.restrict_chat_member(update.message.chat.id, user_id, can_send_messages=False)
                await update.message.reply_text(f"User {user_id} has been muted.")
                log_interaction(update.message.text, f"User {user_id} has been muted.")
            except ValueError:
                await update.message.reply_text("Invalid user ID. Please provide a valid numeric user ID.")
        else:
            await update.message.reply_text("Please provide a user ID to mute.")
    else:
        await update.message.reply_text("This command only works in groups.")

# Define the unmute command for groups
async def unmute_command(update: Update, context: CallbackContext):
    """Unmute a user in the group."""
    if update.message.chat.type != 'private':
        if context.args:
            try:
                user_id = int(context.args[0])  # user ID should be provided after the command
                await context.bot.restrict_chat_member(update.message.chat.id, user_id, can_send_messages=True)
                await update.message.reply_text(f"User {user_id} has been unmuted.")
                log_interaction(update.message.text, f"User {user_id} has been unmuted.")
            except ValueError:
                await update.message.reply_text("Invalid user ID. Please provide a valid numeric user ID.")
        else:
            await update.message.reply_text("Please provide a user ID to unmute.")
    else:
        await update.message.reply_text("This command only works in groups.")

# Define the kick command for groups
async def kick_command(update: Update, context: CallbackContext):
    """Kick a naughty user from the group."""
    if update.message.chat.type != 'private':
        if context.args:
            try:
                user_id = int(context.args[0])  # user ID should be provided after the command
                await context.bot.kick_chat_member(update.message.chat.id, user_id)
                await update.message.reply_text(f"User {user_id} has been kicked from the group.")
                log_interaction(update.message.text, f"User {user_id} has been kicked from the group.")
            except ValueError:
                await update.message.reply_text("Invalid user ID. Please provide a valid numeric user ID.")
        else:
            await update.message.reply_text("Please provide a user ID to kick.")
    else:
        await update.message.reply_text("This command only works in groups.")

# Define the ban command for groups
async def ban_command(update: Update, context: CallbackContext):
    """Ban a user from the group."""
    if update.message.chat.type != 'private':
        if context.args:
            try:
                user_id = int(context.args[0])  # user ID should be provided after the command
                await context.bot.ban_chat_member(update.message.chat.id, user_id)
                await update.message.reply_text(f"User {user_id} has been banned from the group.")
                log_interaction(update.message.text, f"User {user_id} has been banned from the group.")
            except ValueError:
                await update.message.reply_text("Invalid user ID. Please provide a valid numeric user ID.")
        else:
            await update.message.reply_text("Please provide a user ID to ban.")
    else:
        await update.message.reply_text("This command only works in groups.")

# Define the hello command
async def hello_command(update: Update, context: CallbackContext):
    """Greet the user in a friendly way."""
    user = update.message.from_user
    greeting = f"Hey {user.first_name}, how's it going? 😊"
    await update.message.reply_text(greeting)
    log_interaction(update.message.text, greeting)

# Handle new users joining a group
async def new_member(update: Update, context: CallbackContext):
    """Greet a new user when they join the group."""
    new_user = update.message.new_chat_members[0]
    await update.message.reply_text(f"Welcome {new_user.first_name}! 😊 Type /help to see what I can do.")
    log_interaction(f"New user {new_user.first_name} joined.", f"Welcome {new_user.first_name}! 😊 Type /help to see what I can do.")

# Define your /imran command
def imran(update: Update, context: CallbackContext):
    """Message to send when the /imran command is triggered."""
    about_me = (
        "All About Me\n"
        "Your Go-To Web Developer & Problem Solver\n\n"
        "Hey there! I’m **Imran Shiundu**, a passionate web developer who’s all about creating smooth, **user-friendly** websites "
        "that leave an impact. I specialize in designing responsive, functional, and visually engaging sites that **empower** businesses "
        "to thrive online. Whether you’re looking for a fresh new website or a complete revamp, I’m here to bring your ideas to life and "
        "make them shine in the digital world. **Let’s team up** and build something unforgettable!"
    )
    
    # Send the message to the user
    update.message.reply_text(about_me, parse_mode='Markdown')
    log_interaction(update.message.text, about_me)

# Define the error handler
async def error_handler(update: Update, context: CallbackContext):
    """Logs errors and sends a user-friendly message."""
    logger.error(f"Update {update} caused error {context.error}")
    await update.message.reply_text("Oops! Something went wrong. Please try again later.")

# Logging interactions
def log_interaction(user_message, bot_response):
    """Logs the interaction between the user and the bot."""
    data = {
        'user_message': user_message,
        'bot_response': bot_response
    }
    with open('bot_logs.json', 'a') as f:
        json.dump(data, f)
        f.write("\n")

# Set up your bot with the token
def main():
    token = '7679364044:AAFuTMyOBzvGLxJrdoIul6wunDgy_TXuotA'

    # Create the Application instance
    application = Application.builder().token(token).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(CommandHandler("joke", joke_command))
    application.add_handler(CommandHandler("quote", quote_command))
    application.add_handler(CommandHandler("calc", calc_command))
    application.add_handler(CommandHandler("mute", mute_command))
    application.add_handler(CommandHandler("unmute", unmute_command))
    application.add_handler(CommandHandler("kick", kick_command))
    application.add_handler(CommandHandler("ban", ban_command))
    application.add_handler(CommandHandler("hello", hello_command))
    application.add_handler(CommandHandler("imran", imran))

    # Register message handler for new members
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))

    # Register error handler
    application.add_error_handler(error_handler)

    # Start polling for updates
    logger.info("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()

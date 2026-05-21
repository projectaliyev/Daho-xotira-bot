🧠 Daho Xotira Bot — Telegram Avtojavob Boti
"""
 
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
 
# ============================================================
BOT_TOKEN = "8755018483:AAENMP0x2djODzhzTL82ygs0kvW1ly7etBI
 "
YOUTUBE_LINK = "https://youtube.com/@projectaliyev7481"
TELEGRAM_GROUP = "https://t.me/+33CWdFhGHYo1ODdi"
 
WELCOME_MESSAGE = """👋 Salom, {ism}!
 
🧠 *Daho Xotira* kanaliga xush kelibsiz!
 
Xotirangizni kuchaytirishga tayyor bo'lgan bo'lsangiz — quyidagi havolalarni bosing:
 
📺 *YouTube* — bepul darslar va texnikalar
👥 *Telegram guruh* — birga o'rganamiz, savol-javob
 
Qo'shiling va xotirangizni rivojlantiring! 💪"""
# ============================================================
 
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
 
 
def build_keyboard():
    keyboard = [
        [InlineKeyboardButton("📺 YouTube Kanal", url=YOUTUBE_LINK)],
        [InlineKeyboardButton("👥 Telegram Guruh", url=TELEGRAM_GROUP)],
    ]
    return InlineKeyboardMarkup(keyboard)
 
 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    ism = user.first_name or "Do'stim"
    await update.message.reply_text(
        WELCOME_MESSAGE.format(ism=ism),
        parse_mode="Markdown",
        reply_markup=build_keyboard(),
    )
    logger.info(f"Start: {user.id} — {ism}")
 
 
async def har_qanday_xabar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    ism = user.first_name or "Do'stim"
    await update.message.reply_text(
        WELCOME_MESSAGE.format(ism=ism),
        parse_mode="Markdown",
        reply_markup=build_keyboard(),
    )
    logger.info(f"Xabar: {user.id} — {ism}")
 
 
def main():
    print("🤖 Daho Xotira Bot ishga tushmoqda...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, har_qanday_xabar))
    print("✅ Bot tayyor!")
    app.run_polling()
 
 
if __name__ == "__main__":
    main()

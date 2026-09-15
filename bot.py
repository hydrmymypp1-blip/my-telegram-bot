import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("bot")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📥 تحميل", "🎵 الأغاني"],
        ["👤 حسابي", "ℹ️ معلومات"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "هلا بيك 👋\nاختار من الأزرار:",
        reply_markup=reply_markup
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📥 تحميل":
        await update.message.reply_text("📥 أرسل الرابط حتى أتعامل وياه.")

    elif text == "🎵 الأغاني":
        await update.message.reply_text("🎵 اختار نوع الأغنية.")

    elif text == "👤 حسابي":
        user = update.effective_user
        await update.message.reply_text(
            f"👤 الاسم: {user.first_name}\n"
            f"🆔 ID: {user.id}"
        )

    elif text == "ℹ️ معلومات":
        await update.message.reply_text(
            "🤖 بوت Telegram\n"
            "تم تشغيله بواسطة Python."
        )

    else:
        await update.message.reply_text("❌ اختار أحد الأزرار الموجودة.")


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN غير موجود")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, buttons)
    )

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
from telegram import Update
from telegram.ext import (
    Application,
    ApplicationHandlerStop,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ChatMemberHandler,
    CallbackQueryHandler,
    filters,
    ConversationHandler
)
from config import BOT_TOKEN

from database import create_tables

# ==================================================
# أسرع كلمة
# ==================================================
from games.speed_words import (
    start_speed_words,
    check_speed_words
)

import os
import asyncio
import threading


# ==================================================
# MAIN
# ==================================================
def main():
    # ==================================================
    # إنشاء الجداول
    # ==================================================
    app = (
        Application
        .token(BOT_TOKEN)
        .build()
    )



    # ==================================================
    # أسرع كلمة
    # ==================================================
    app.add_handler(
        MessageHandler(
            filters.Regex(r"^كلمات$"),
            start_speed_words
        )
    )
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            check_speed_words
        ),
        group=50
    )

    # ==================================================
    # تشغيل البوت
    # ==================================================
    print("🤖 Bot Started...")
    threading.Thread(
        target=start_web_server,
        daemon=True
    ).start()
    app.run_polling()
# ==================================================
# التشغيل
# ==================================================
if __name__ == "__main__":
    main()

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# إعداد السجلات (Logging) لمتابعة حالة البوت
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# توكن البوت الخاص بك
TOKEN = '8321239413:AAHta_69G0xEat_QjEL2iLLYVDrdu2Vrvhw'

async def reply_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """هذه الدالة ترد على أي رسالة تصل للبوت"""
    await update.message.reply_text("هاهيه ولك😂")

if __name__ == '__main__':
    # بناء التطبيق وربطه بالتوكن
    application = ApplicationBuilder().token(TOKEN).build()
    
    # إضافة معالج للرسائل (يسمع لأي نص أو صورة أو ملف)
    echo_handler = MessageHandler(filters.ALL, reply_handler)
    application.add_handler(echo_handler)
    
    print("البوت شغال الآن... أرسل له أي شيء!")
    
    # بدء تشغيل البوت
    application.run_polling()

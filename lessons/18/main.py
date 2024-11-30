import os
from email_sender import EmailSender
from telegram import Telegram
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    
    #email sending:
    email_sender = EmailSender(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        sender_email="nigrushid@gmail.com",
        sender_password=os.environ.get("GMAIL_PW")
    )
    html_body = email_sender.render_email_template("lessons/18/email_template.html",
                                                   {"user_name": "Tóbiás",
                                                    "year": 2024})

    email_sender.send_email(
        recipients=["nigrushid@gmail.com"],
        subject="Test Email",
        body= html_body, #"Szia",
        attachments=["lessons/18/to_send.csv"]
    )

    #telegram message sending:

    telegram = Telegram(os.environ.get("TELEGRAM_BOT_TOKEN"),
                        os.environ.get("TELEGRAM_CHAT_ID"))
    
    telegram.send_telegram_message("This is a test message from the course.")
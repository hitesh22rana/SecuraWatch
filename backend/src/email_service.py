from datetime import datetime
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.config import settings


class EmailService:
    smtp_server: str = settings.smtp_host
    smtp_port: int = settings.smtp_port
    user: str = settings.smtp_username
    password: str = settings.smtp_password

    server: smtplib.SMTP = None
    last_activity_time: float = None
    timeout: int = 300

    @classmethod
    def __init__(cls):
        cls._login()

    @classmethod
    def _login(cls):
        try:
            if not cls.server:
                cls.server = smtplib.SMTP(cls.smtp_server, cls.smtp_port)
                cls.server.starttls()
                cls.server.login(cls.user, cls.password)

        except smtplib.SMTPException as e:
            print(e)

        except Exception as e:
            print(e)

    @classmethod
    def _check_connection(cls):
        if cls.last_activity_time is None:
            cls._reconnect()
            cls.last_activity_time = time.time()

        current_time = time.time()
        elapsed_time = current_time - cls.last_activity_time

        if elapsed_time >= cls.timeout:
            cls._reconnect()
        else:
            cls.last_activity_time = current_time

    @classmethod
    def _reconnect(cls):
        cls.server.quit()
        cls.server = None
        cls.last_activity_time = None
        cls._login()

    @classmethod
    def send_email(cls, recipient: str, subject: str, message: str):
        cls._check_connection()

        try:
            msg = MIMEMultipart("alternative")

            msg["Subject"] = subject
            msg["From"] = cls.user
            msg["To"] = recipient

            msg.attach(MIMEText(message))

            cls.server.sendmail(cls.user, recipient, msg.as_string())
            cls.last_activity_time = time.time()

        except smtplib.SMTPException as e:
            print(e)

        except Exception as e:
            print(e)

    @classmethod
    def send_intrusion_notification(cls, file_id: str, recipient: str):
        cls.send_email(
            recipient=recipient,
            subject=(
                f"Intrusion Detected at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
            ),
            message=f"Intrusion detected in file {file_id}",
        )


email_service = EmailService()

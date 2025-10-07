import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your-email@example.com"
SMTP_PASSWORD = "password"  # use env vars in production!


def send_email(to_email: str, subject: str, body: str):
    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        from app.core.logging import log_error

        log_error(f"Email sending failed: {e}")

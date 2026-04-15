import smtplib
import os

class NotificationManager:
    def __init__(self):
        self.smtp_address = os.environ.get("EMAIL_PROVIDER_SMTP_ADDRESS")
        self.email = os.environ.get("MY_EMAIL")
        self.email_password = os.environ.get("MY_EMAIL_PASSWORD")

    def send_emails(self, email_list, email_body):
        # Open connection only when needed
        with smtplib.SMTP(self.smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(self.email, self.email_password)
            for email in email_list:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )